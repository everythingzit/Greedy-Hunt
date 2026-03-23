import json
from datetime import date
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
            page.wait_for_selector(".ashby-job-posting-brief", timeout=15000)

            scraped_jobs = page.query_selector_all("._container_j2da7_1")
            base = self.company["url"]["base"]
            urls = [base + job.get_attribute("href") for job in scraped_jobs]
            for url in urls:
                page.goto(url)
                schema_el = page.query_selector('script[type="application/ld+json"]')
                context = json.loads(schema_el.inner_text())
                date_posted = context["datePosted"].strip()
                today = str(date.today())
                
                if today != date_posted:
                    title = page.query_selector("h1._title_ud4nd_34").inner_text()
                    company = self.company["company"]
                    location = page.query_selector("div._section_101oc_37").query_selector("p").inner_text()

                    job_match = Job(title, company, location, url, date_posted)
                    jobs.append(job_match)

            browser.close()

        return jobs