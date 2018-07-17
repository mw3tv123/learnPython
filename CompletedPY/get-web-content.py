# Get contents from a web site
import requests
url = 'http://www.nytimes.com/'
response = requests.get(url)
contents = response.text

# Filter out contents
from bs4 import BeautifulSoup
soup = BeautifulSoup(contents, "lxml")
for story_heading in soup.find_all(class_="story-heading"):
	if story_heading.a:
		print(story_heading.a.text.replace("\n", " ").strip())
	else:
		print(story_heading.contents[0].strip())
