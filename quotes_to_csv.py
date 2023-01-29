from bs4 import BeautifulSoup
import requests
import csv

url = "http://quotes.toscrape.com"
response = requests.get(url, headers={'Accept-Encoding': 'utf-8'})
soup = BeautifulSoup(response.content, 'html.parser')

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

with open('quotes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author', 'Tags'])
    for i in range(len(quotes)):
        quote_tags = [tag.text for tag in tags[i].find_all('a', class_='tag')]
        writer.writerow([quotes[i].text, authors[i].text, quote_tags])
