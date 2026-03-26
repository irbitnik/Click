from bs4 import BeautifulSoup
import re

my_power = float(input('Мощность моих майнеров Ph/s: '))
miners = {}

for html in iter(input, 'end'):

    soup = BeautifulSoup(html, 'html.parser')

    cards = soup.find_all('a', class_='marketplace-buy-item-card')

    for card in cards:

        title = card.find('p', class_='item-title').get_text(strip=True)

        price = card.find('p', class_='item-price').get_text(strip=True)
        price1 = float(re.sub(r'RLT', '', price).strip())

        bonus = card.find('span', class_='item-addition-bonus').get_text(strip=True)
        bonus1 = float(re.sub(r'%', '', bonus).strip()) / 100

        power = card.find('span', class_='item-addition-power').get_text(strip=True)

        if 'Gh/s' in power:
            power1 = float(re.sub(r'Gh/s', '', power).strip()) / 1000000
        if 'Th/s' in power:
            power1 = float(re.sub(r'Th/s', '', power).strip()) / 1000
        if 'Ph/s' in power:
            power1 = float(re.sub(r'Ph/s', '', power).strip())

        power2 = (power1 + (power1 + my_power)*bonus1) / price1

        miners[title] = power2
        print(f'Добавляю {title} {power2}')

best_miner = max(miners.items(), key=lambda x: x[1])
print(best_miner)


