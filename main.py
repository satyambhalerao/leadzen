from bs4 import BeautifulSoup
import requests
import csv
import os.path
URL = ("https://www.amazon.in/s?k=bags&page=20&ref=sr_pg_20")
HEADER = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 44.0.2403.157 Safari / 537.36','Accept-Language': 'en-US, en;q=0.5'}
while(True):
    webpage = requests.get(URL,headers=HEADER)
    if(webpage.status_code == 200):
        print("5")
        soup = BeautifulSoup(webpage.text, 'lxml')
        print(webpage.status_code)

        Name = []
        price = []
        URL = []

        for i in soup.find_all('a',class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'):
            Name.append(i.text)
        print(Name)
        for i in soup.find_all('span',class_='a-price-whole'):
            price.append(i.text)
        print(price)
        for i in soup.find_all('a',class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'):
            URL.append("https://www.amazon.in"+i.get('href'))
        print(URL)
        file_name = "amazon_page20.csv"

        with open(file_name,'a',encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['Sr.No','Name','Price','URL'])
            for i in range(0, 21):
                writer.writerow([i+1,Name[i],price[i],URL[i]])
        break





