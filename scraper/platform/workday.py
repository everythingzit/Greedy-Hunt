from playwright.sync_api import sync_playwright
from scraper.base import BaseScraper
from scraper.job import Job

class WorkdayScraper(BaseScraper):
    def scrape(self) -> list[Job]:
        jobs = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(self.company["url"]["workday"])
            page.wait_for_selector("li.css-1q2dra3", timeout=15000)
            
            scraped_jobs = page.query_selector_all(".css-1q2dra3")
            for job in scraped_jobs:
                title = job.query_selector('[data-automation-id="jobTitle"]').inner_text()
                company = self.company["company"]
                location_container = job.query_selector('[data-automation-id="locations"]')
                location = location_container.query_selector("dd.css-129m7dg").inner_text()
                base = self.company["url"]["base"]
                url = base + job.query_selector("a").get_attribute("href")
                date_container = job.query_selector('[data-automation-id="postedOn"]')
                date_posted = date_container.query_selector("dd.css-129m7dg").inner_text()

                time_selectors = ["today"]
                if any(word in date_posted.lower() for word in time_selectors):
                    job_match = Job(title, company, location, url, date_posted)
                    jobs.append(job_match)

            browser.close()

        return jobs