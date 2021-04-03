from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/CLABE'

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

output = BeautifulSoup(html, features='html.parser')
table = output.find('table', attrs='wikitable')

cells = []

for row in table.findAll('tr'):
    for cell in row.findAll('td'):
        nextVal = cell.text
        #print(nextVal)
        cells.append(nextVal)
    
print(cells)

""" outputFile = open('./banks.csv', 'w')
writer = csv.writer(outputFile)
writer.writerows(cells) """