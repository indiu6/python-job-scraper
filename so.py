import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    # print(last_page)

    return int(last_page)


def extract_job(html):
    title = html.find("h2", {"class": "mb4"}).find("a")["title"]
    # print(title)
    company, location = html.find("h3", {"class": "fc-black-700"}).find_all(
        "span", recursive=0  # 0 = False, 1 = True
    )
    company = company.get_text(strip=1)
    location = location.get_text(strip=1)
    # print(company, location)
    job_id = html["data-jobid"]

    return {
        "title": title,
        "company": company,
        "location": location,
        "apply_link": f"https://stackoverflow.com/jobs/{job_id}",
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: Page: {page}")
        result = requests.get(f"{URL}pg={page + 1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            # print(result["data-jobid"])
            job = extract_job(result)
            # print(job)
            jobs.append(job)

    return jobs


def get_jobs():
    last_page = get_last_page()
    # print(last_page)
    jobs = extract_jobs(last_page)

    return jobs
