import requests
from bs4 import BeautifulSoup
import csv

url = input('Please provide Trulia url you want to scrape:\t')
pages = requests.get(url).text
s = BeautifulSoup(pages, 'html.parser')
btns = s.find_all('a', class_='ButtonBase-sc-14ooajz-0 PaginationButton-sc-1yuoxn6-1 fea-DjF')
page = [btn.get_text() for btn in btns]
ran = page[-1]

print('Pages number is: ' + str(ran))

ads = {}

for i in range(1, int(ran)+1):
    try:
        response= requests.get(url+f'{i}_p/').text
        print(url+f'{i}_p/')
        soup = BeautifulSoup(response, 'html.parser')
        data = soup.find('ul', class_='Grid__GridContainer-sc-144isrp-1 bQSVOQ')
        lsts = data.find_all('li')

        for l in lsts:
            beds = l.find('div', attrs={'data-testid': 'property-beds'})
            price = l.find('div', attrs={'data-testid':'property-price'})
            baths= l.find('div', attrs={'data-testid': 'property-baths'})
            fspace = l.find('div', attrs={'data-testid': 'property-floorSpace'})
            address = l.find('div', attrs={'data-testid': 'property-address'})
            link = l.find('a', attrs={'class':'Anchor__StyledAnchor-sc-5lya7g-1 gLFHbk'})
            try:
                print(price.get_text())
                print(beds.get_text())
                print(baths.get_text())
                print(fspace.get_text())
                print(address.get_text())
                print('https://www.trulia.com'+link['href'])
                with open('listing.csv', 'a+') as file:
                    writer = csv.writer(file)

                    writer.writerow([price.get_text(), beds.get_text(), baths.get_text(), fspace.get_text(), address.get_text(),'https://www.trulia.com'+link['href']])

            except AttributeError:
                continue
    except :
        print('All done')
