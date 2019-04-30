"""
  get all pokemon sprite from https://pokemondb.net/pokedex/national
"""
import requests
from bs4 import BeautifulSoup

r = requests.get("https://pokemondb.net/pokedex/national")
soup = BeautifulSoup(r.text, "html.parser")

cards = soup.find_all("div", class_="infocard")

for card in cards:
    img = card.find("span", class_="img-sprite")
    img_url = img['data-src']
    no = card.find('span', class_='infocard-lg-data').find('small').text[1:]
    print(no)
    r = requests.get(img_url)
    with open('./img/' + no + '.jpg', mode='wb') as f:
        f.write(r.content)
