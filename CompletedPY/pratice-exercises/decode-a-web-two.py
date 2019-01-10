# Get contents of the website
import requests
def getWebContents(url):
	html_contents = requests.get(url);
	return html_contents.text

# Take needed contents
from bs4 import BeautifulSoup
def getNeededElement(html_text):
	soup = BeautifulSoup(html_text, "lxml")
	for element in soup.select("div.parbase.cn_text > div.body > p "):
		print(element.text)
	return	"".join(soup.select("div.parbase.cn_text > div.body > p"))

if __name__ == "__main__":
	url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
	result = getNeededElement(getWebContents(url))
	
