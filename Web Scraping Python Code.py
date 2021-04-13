import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = requests.get('http://www.census.gov/programs-surveys/popest.html')
text = URL.text

soup = BeautifulSoup(text, 'html.parser')

links = []
for url in soup.find_all('a'):
    link = urljoin('https://www.census.gov/programs-surveys/popest.html',url.get('href'))
    if link not in links:
        links.append(link)

import csv
j=[["Unique Links"]]
k=[["Links"]]
with open('C:\\Users\\david\\Desktop\\Export File\\Links from Census Data.csv','w', newline='') as f:
    cw =csv.writer(f)
    cw.writerow(j)
    cw.writerow(k)
    cw.writerow(links)

f.close()
print(links)
