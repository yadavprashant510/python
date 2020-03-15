from bs4 import BeautifulSoup as soup
from urllib import request

url = "https://www.flipkart.com"
get_url = request.urlopen(url)
content = soup(get_url, "lxml")
print(soup.prettify(content))
print("------------------------------------")
print(f"Title :{soup.title.name}")
# print(f"Title name: {soup.title.name}")
# print(f"Title Text: {soup.title.string}")
# print(f"Title parent name: {soup.title.parent.name}")
# print(f"Paragraph tag name: {soup.p}")
# print(f"Attribute name: {soup.find_all('a')}")
# top_smrt = soup.findAll("h2")[0]
# print(top_smrt)
# print(f"Search Box: {soup.find(id='twotabsearchtextbox')}")
# print(soup.get_text())