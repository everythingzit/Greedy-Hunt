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
            page.wait_for_selector('[data-automation-id="jobResults"]', timeout=15000)
            title = page.title()

            browser.close()

        return title