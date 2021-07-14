import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
  result = requests.get(URL)

  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"class": "pagination"})

  links = pagination("a")
  pages = []
  for link in links[:-1]:
    pages.append(int(link.find("span").string))

  max_page = pages[-1]

  return max_page


def extract_job(html):
  job_title = html.find("h2", {"class" : "jobTitle"})
  title = job_title.find("span").string
  if title == "new":
    title = job_title.find_all("span")[1].string

  company_name = html.find("span", {"class":"companyName"})
  company_anchor = company_name.find("a")
  if company_anchor is None:
    company_name = str(company_name.string)
  else:
    company_name = str(company_anchor.string)
  company_name = company_name.strip()

  # company_location = html.find("div", {"class":"companyLocation"})
  company_location = html.select_one("pre > div").text

  job_id = html['data-jk']
  
  return {'title' : title, 'company_name' : company_name, 'company_location' : company_location, 'link' : f"https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"}


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping page: {page}")
    result = requests.get(f"{URL}&start={page * LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup("a", {"class": "fs-unmask"})

    for result in results:
      job = extract_job(result)
      jobs.append(job)

  return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs


