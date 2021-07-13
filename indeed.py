import requests
from bs4 import BeautifulSoup

LIMIT = 50

URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)
  # print(indeed_result.text)

  soup = BeautifulSoup(result.text, "html.parser")
  # print(indeed_soup)

  pagination = soup.find("div", {"class": "pagination"})
  # print(pagination)

  links = pagination("a")
  pages = []
  for link in links[:-1]:
    pages.append(int(link.find("span").string))
  # print(pages)

  max_page = pages[-1]
  # print(range(max_page))

  return max_page


def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}&start={0 * LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup("a", {"class": "fs-unmask"})

  for result in results:
    job_title = result.find("h2", {"class" : "jobTitle"})
    title = job_title.find("span").string
    if title == "new":
      title = job_title.find_all("span")[1].string
    # print(title)

    company_name = result.find("span", {"class":"companyName"})
    company_anchor = company_name.find("a")
    if company_anchor is None:
      company_name = str(company_name.string)
    else:
      company_name = str(company_anchor.string)
    company_name = company_name.strip()
    print(title, company_name)

  return jobs


