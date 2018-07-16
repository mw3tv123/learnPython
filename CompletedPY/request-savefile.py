import requests, datetime
from bs4 import BeautifulSoup

# Getting contents of the HTML page
def get_contents(url = ""):
	r = requests.get(url)
	return r.text

# Saving contents to file text
def saveLog(_contents_ = " "):
	with open("log.txt", "at") as f:
		x = str(datetime.datetime.now())
		x += "\n" + _contents_
		f.write(x)

# Handle the title
link = raw_input("Enter your url: ")
soup = BeautifulSoup(get_contents(link), "lxml")
all_story_heading = soup.find_all(class_="story-heading")
contents = "".encode("utf-8")
for story_heading in all_story_heading:
	if story_heading.a:
		contents += story_heading.a.text.replace("\n", " ").strip().encode("utf-8")
	else:
		contents += story_heading.contents[0].strip().encode("utf-8")
saveLog(contents)
