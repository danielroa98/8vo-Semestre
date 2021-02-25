import requests
from bs4 import BeautifulSoup

response = requests.get('http://whatweekisit.com/')
response.status_code

soup = BeautifulSoup(response.content, 'html.parser')

print(soup)