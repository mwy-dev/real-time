import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup
import csv

def real_time_price():
    url = ('https://www.msn.com/en-us/money/stockdetails/nas-aapl/fi-a1mou2?duration=1D')
    r = requests.get(url)
    
    web_content = BeautifulSoup(r.text, 'lxml')
    web_content = web_content.find('span', {"class":'currentval'}).text

    return web_content

Date = datetime.datetime.now()
Date = Date.strftime("%Y-%m-%d/%H:%M:%S")
value = []
wyniki = []
value.append(real_time_price())
wyniki = [Date]
wyniki.extend(value)
Date = wyniki[0]
AAPL = wyniki[1]
df = pd.DataFrame({'Date': [wyniki[0]], 'Value': [wyniki[1]]})
i=0
k=0

fieldnames = ["Date", "AAPL"]

with open('real time stock data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open('real time stock data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "Date": Date,
            "AAPL": AAPL
        }

        csv_writer.writerow(info)
        Date = datetime.datetime.now()
        Date = Date.strftime("%Y-%m-%d/%H:%M:%S")
        value = []
        wyniki = []
        value.append(real_time_price())
        wyniki = [Date]
        wyniki.extend(value)
        df = pd.DataFrame(wyniki)
        Date = wyniki[0]
        AAPL = wyniki[1]
        print(wyniki)
        
        while i<1:
            if float(AAPL) > 133:
                requests.post("https://api.mailgun.net/v3/sandboxda15bf2f0c90448e9d52c51634a704da.mailgun.org/messages",
                          auth=("api", "53c17cf7efbfaea761dbf5e848be4001-523596d9-8e1498bc"),
                          data={"from": "Mailgun Sandbox <postmaster@sandboxda15bf2f0c90448e9d52c51634a704da.mailgun.org>",
                                "to": "RTA <rta.sgh2022@gmail.com>",
                                "subject": "RTA TEST-RISE",
                                "text": "Your stock price is rising!"})
                i=1
        while k<1:
            if float(AAPL) < 140:
                requests.post("https://api.mailgun.net/v3/sandboxda15bf2f0c90448e9d52c51634a704da.mailgun.org/messages",
                          auth=("api", "53c17cf7efbfaea761dbf5e848be4001-523596d9-8e1498bc"),
                          data={"from": "Mailgun Sandbox <postmaster@sandboxda15bf2f0c90448e9d52c51634a704da.mailgun.org>",
                                "to": "RTA <rta.sgh2022@gmail.com>",
                                "subject": "RTA TEST-FALL",
                                "text": "Your stock price is falling!"})
                k=1