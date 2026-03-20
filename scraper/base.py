from abc import ABC, abstractmethod

class BaseScraper(ABC):
    def __init__(self, company: dict):
        self.company = company

    @abstractmethod
    def scrape(self) -> list[dict]:
        pass