import pandas as pd
import requests
import csv
from bs4 import BeautifulSoup

name = []
rating = []
reviews = []
manufacture = []
ASIN = []
for i in range(1, 21):
    filename = "amazon_page"+str(i)+"_addition.csv"
    data = pd.read_csv(r"amazon_page"+str(i)+".csv")
    HEADER = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 44.0.2403.157 Safari / 537.36',
        'Accept-Language': 'en-US, en;q=0.5'}

    lists = list(data['URL'].values)
    for i in lists[:21]:
        print("extracting.......")
        webpage = requests.get(i, headers=HEADER)
        soup = BeautifulSoup(webpage.text, 'lxml')
        name_tag = soup.find('span', attrs={'id': 'productTitle'})
        name_text = name_tag.text.strip() if name_tag else ""
        name.append(name_text)

        # Extract rating
        rating_tag = soup.find('span', attrs={'class': 'a-size-base a-color-base'})
        rating_text = rating_tag.text.strip() if rating_tag else ""
        rating.append(rating_text)

        # Extract reviews
        reviews_tag = soup.find('span', attrs={'id': 'acrCustomerReviewText'})
        reviews_text = reviews_tag.text.strip() if reviews_tag else ""
        reviews.append(reviews_text)

        # Extract manufacture
        manufacture_tag = soup.find('div', attrs={'id': 'detailBullets_feature_div'})
        if manufacture_tag:
            manufacture_spans = manufacture_tag.find_all('span', attrs={'class': 'a-list-item'})
            if len(manufacture_spans) >= 3:
                manufacture_text = manufacture_spans[2].find_next('span').find_next_sibling('span').text.strip()
                manufacture.append(manufacture_text)
            else:
                manufacture.append("")
        else:
            manufacture.append("")

        # Extract ASIN
        ASIN_tag = soup.find('div', attrs={'id': 'detailBullets_feature_div'})
        if ASIN_tag:
            ASIN_spans = ASIN_tag.find_all('span', attrs={'class': 'a-list-item'})
            if len(ASIN_spans) >= 4:
                ASIN_text = ASIN_spans[3].find_next('span').find_next_sibling('span').text.strip()
                ASIN.append(ASIN_text)
            else:
                ASIN.append("")
        else:
            ASIN.append("")

    for i in range(0, 21):
        print(i)
        with open(filename, 'a', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['Sr.No', 'Name', 'Rating', 'Reviews', 'Manufacture', 'ASIN'])
            writer.writerow([i + 1, name[i], rating[i], reviews[i], manufacture[i], ASIN[i]])
    name.clear()
    rating.clear()
    reviews.clear()
    manufacture.clear()
    ASIN.clear()