# import requests
# from bs4 import BeautifulSoup
# def find_user_product():
#     find_prod = input('Введите продукт, который хотите найти: ')
#     source = requests.get('https://www.avito.ru/cheboksary?q=' + find_prod).text
#
#     soup = BeautifulSoup(source, 'html.parser')
#
#     for div in soup.find_all('div', class_='iva-item-body-KLUuy'):
#         url = div.find('div', 'iva-item-titleStep-pdebR').a
#         print(url['title'], '\n' + 'https://www.avito.ru' + url['href'])
#         price = div.find('div', 'iva-item-priceStep-uq2CQ').span
#         print(price.text, '\n')
# find_user_product()
