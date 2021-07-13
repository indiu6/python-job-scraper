import requests
from bs4 import BeautifulSoup

INDEED_URL = "https://www.indeed.com/jobs?q=python&limit=50"

def extgract_indeed_pages():
  result = requests.get(INDEED_URL)
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