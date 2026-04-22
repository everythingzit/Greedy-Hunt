from playwright.sync_api import sync_playwright
from scraper.base import BaseScraper
from scraper.job import Job

class Scraper(BaseScraper):
    def scrape(self) -> list[Job]:
        jobs = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(self.company["url"]["company"])
            page.wait_for_selector('[data-test-id="job-listing"]', timeout=15000)

            scraped_jobs = page.query_selector_all('[data-test-id="job-listing"]')
            for job in scraped_jobs:
                title = job.query_selector(".title-1aNJK").inner_text()
                company = self.company["company"]
                location = job.query_selector(".fieldValue-3kEar").inner_text()
                base = "https://apply.careers.microsoft.com"
                url = base + job.query_selector("a.r-link").get_attribute("href")
                date_posted = job.query_selector(".subData-13Lm1").inner_text()

                time_selectors = ["minute", "minutes", "hour", "hours"]
                if any(word in date_posted.lower() for word in time_selectors):
                    job_match = Job(title, company, location, url, date_posted)
                    jobs.append(job_match)

            browser.close()

        return jobs