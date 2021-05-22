import requests
from bs4 import BeautifulSoup

url = 'https://store.steampowered.com/search/?filter=topsellers&os=win'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
top_seller = soup.find_all('a',attrs={'class':'search_result_row ds_collapse_flag'})

for top_game in top_seller:
    title = top_game.find('span', attrs={'class': 'title'}).text
    tanggal = top_game.find('div', attrs={'class': 'col search_released responsive_secondrow'}).text
    image = top_game.find('div', attrs={'class':'col search_capsule'}).find({'img'})
    # harga = top_game.find('div', attrs={'class': 'col search_price responsive_secondrow'})
    #
    # if harga == None:
    #     harga = top_game.find('div', attrs={'class': 'col search_price discounted responsive_secondrow'})
    #
    # print('title: {}'.format(title), ' | date: {}'.format(tanggal), ' | price: {}'.format(harga.text))
    print('title: {}'.format(title), ' | date: {}'.format(tanggal), ' | image: {}'.format(image))