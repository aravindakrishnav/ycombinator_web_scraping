from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
from prettytable import PrettyTable

wb = Workbook()
ws = wb.active

x = PrettyTable()
page = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(page.text, 'html.parser')

articles = soup.find_all(name="tr", class_='athing')

article_text = []
article_link = []
article_rank = []

for article in articles:
    text = article.find('span', class_='titleline').text
    article_text.append(text)
    link = article.find('span', class_='titleline').a.get('href')
    article_link.append(link)
    rank = int(article.find('span', class_='rank').text.split('.')[0])
    article_rank.append(rank)


upvotes = [int(score.getText().split()[0]) for score in soup.find_all('span', class_='score')]

x.add_column('Rank', article_rank)
x.add_column('Title', article_text)
x.add_column('Website', article_link)
x.align["Title"] = "l"
x.align["Website"] = "l"
print(x)

