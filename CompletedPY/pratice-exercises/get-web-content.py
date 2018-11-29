# Import library
import argparse
import requests


def parse_destination_url():
	parser = argparse.ArgumentParser(description='Get contents from URL and save it into a file.')
	parser.add_argument('-u', '--url', type=str, nargs='?', help='URL of the host')
	return parser.parse_args()


def create_connection(url):
	return requests.get(url)


def parse_html_content(response):
	return response.text


def store_download_file(data, file):
	f = open(file, 'w')
	f.write(data)
	f.close()


def main():
	store_download_file(parse_html_content(create_connection(parse_destination_url().url)), 'output.txt')


if __name__ == "__main__":
	main()
