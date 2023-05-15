import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_website_text(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    text = soup.get_text()

    return text


def save_text_to_file(text, filename):

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f"Text saved as {filename}")


website_url = input("Enter the website URL: ")

website_text = get_website_text(website_url)

parsed_url = urlparse(website_url)
website_name = parsed_url.netloc

filename = ''.join(c for c in website_name if c.isalnum()) + ".txt"

save_text_to_file(website_text, filename)
