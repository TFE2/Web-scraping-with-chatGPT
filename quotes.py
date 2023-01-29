from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com"
response = requests.get(url, headers={'Accept-Encoding': 'utf-8'})
soup = BeautifulSoup(response.content, 'html.parser')

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('a', class_='tag')

for i in range(len(quotes)):
    print(f'{quotes[i].text} - {authors[i].text}')
    quote_tags = soup.find_all('a', class_='tag')
    tag_list=[]
    for tag in quote_tags:
        tag_list.append(tag.text)
    print(f'Tags: {tag_list}')
