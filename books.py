from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    link = url + book.h3.a['href']
    print("Title:", title)
    print("Price:", price)
    print("Link:", link)
