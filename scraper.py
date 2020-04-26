import requests
from bs4 import BeautifulSoup
from csv import writer

with open('result.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['Name', 'Price', 'Rating'])

    for page_number in range(1, 22):
        url = f'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page_number}'

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        products = soup.find_all('div', class_="_1-2Iqu")

        for product in products:
            try:
                title = product.find('div', class_="_3wU53n").get_text()
            except:
                title = 'None'

            try:
                price = product.find('div', class_="_1vC4OE _2rQ-NK").get_text().replace('₹', '')
            except:
                price = '-'

            try:
                rating = product.find('div', class_="hGSR34").get_text()
            except:
                rating = 'No ratings'

            csv_writer.writerow([title, price, rating])
