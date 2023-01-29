from bs4 import BeautifulSoup
import requests
import csv

url = "http://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find_all('article', class_='product_pod')

with open('books.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Link'])
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        link = url + book.h3.a['href']
        writer.writerow([title, price, link])
