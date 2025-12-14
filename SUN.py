import requests as req
import json as j
from bs4 import BeautifulSoup

# url_balloon: str = 'https://sfl.tools/api/listings/prices'
# url_nitty: str = 'https://api.sflinfo.tech/api/niftyswap/prices'
# list_item_balloon = ['201', '202', '203', '204', '205', '206', '207', '208', '215', '216', '209',
#                      '210', '211', '213', '214', '212', '601', '602', '605']
# list_item_nitty = ['Sunflower', 'Potato', 'Pumpkin', 'Carrot', 'Cabbage', 'Beetroot', 'Cauliflower', 'Parsnip', 'Eggplant',
#                    'Corn', 'Radish', 'Wheat', 'Kale', 'Blueberry', 'Orange', 'Apple', 'Wood', 'Stone', 'Egg']
#
#

#
#
# def get_price() -> None:
#     date = f'{input("Месяц ")}-{input("Число ")}'
#     print('Ресурс    BALLOON    NITTY')
#     info_balloon = j.loads(BeautifulSoup(get_html(url_balloon), 'lxml').p.text)
#     info_nitty = j.loads(BeautifulSoup(get_html(url_nitty), 'lxml').p.text)
#
#     for i in range(19):
#         item_balloon = info_balloon[list_item_balloon[i]]
#         if list_item_nitty[i] != 'Corn' and list_item_nitty[i] != 'Apple':
#             item_nitty = info_nitty[list_item_nitty[i]]
#             print(item_balloon['sflItemName'], item_balloon['pricePerUnitTaxed'].replace('.', ',')[:6], '   ', str(item_nitty[date]).replace('.', ',')[:6])
#         else:
#             print(item_balloon['sflItemName'], item_balloon['pricePerUnitTaxed'].replace('.', ',')[:6])
#
#
# if __name__ == '__main__':
#     get_price()


class SFL:

    url = "https://sfl.world/api/v1/prices"
    price_coin = 0.001194
    prices = req.get(url).json()['data']['p2p']




print()
