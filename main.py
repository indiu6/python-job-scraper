import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
# print(indeed_result.text)

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
# print(indeed_soup)

pagination = indeed_soup.find("div", {"class": "pagination"})
# print(pagination)

pages = pagination("a")
spans = []
for page in pages:
  spans.append(page.find("span"))
print(spans[:-1])
spans = spans[:-1]

