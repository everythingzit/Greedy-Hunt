import yaml
import importlib
from scraper.base import BaseScraper
from scraper.job import Job

def load_companies() -> list[dict]:
    with open("config/companies.yml", "r") as file:
        try:
            companies = yaml.safe_load(file)
            return companies
        except yaml.YAMLError as exc:
            print(exc)

def match_scrapers(company: dict) -> BaseScraper:
    scrapers = []

    if company["platform"] == "workday":
        module = importlib.import_module("scraper.platform.workday")
        scrapers.append(module.WorkdayScraper(company))

    if company["custom"]:
        module = importlib.import_module(f"scraper.custom.{company["module"]}")
        scrapers.append(module.Scraper(company))

    return scrapers

def process_data(jobs: list[Job]):
    pass

def main():
    jobs = []

    companies = load_companies()
    for company in companies:
        if company["company"] == "Wealthsimple":
            scrapers = match_scrapers(company)
            for scraper in scrapers:
                output = scraper.scrape()
                jobs.extend(output)

                # for job in output:
                #     print(f"{job.title} | {job.company} | {job.url}")
                    
if __name__=="__main__":
    main()