from scraper.base import BaseScraper
from scraper.job import Job

class GreenhouseScraper(BaseScraper):
    def scrape(self) -> list[Job]:
        return self.company["company"] + " --- GREENHOUSE"