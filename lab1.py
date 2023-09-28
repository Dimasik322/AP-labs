import os
import json
import requests
import csv
import time
from bs4 import BeautifulSoup

URL = "https://www.cbr-xml-daily.ru/"
htmlPage = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
soup = BeautifulSoup(htmlPage.text, "html.parser")
allURLs = soup.findAll("a", class_="")
URL = URL + allURLs[6]["href"]
file = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"}).json()
date = file['Date']
value = file['Valute']['USD']['Value']
previous_URL = file['PreviousURL']
print("https:"+previous_URL)

with open('dataset.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Date', 'Value'])
    filewriter.writerow([date[:10], value])
    for i in range(10000):
        #time.sleep(0.51)
        URL = 'https:' + previous_URL
        file = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"}).json()
        date = file['Date']
        value = file['Valute']['USD']['Value']
        print(date[:10], value)
        previous_URL = file['PreviousURL']
        filewriter.writerow([date[:10], value])