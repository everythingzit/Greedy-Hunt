from scraper.base import BaseScraper
from scraper.job import Job

class Scraper(BaseScraper):
    def scrape(self) -> list[Job]:
        return []