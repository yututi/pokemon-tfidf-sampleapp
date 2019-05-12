import requests
from bs4 import BeautifulSoup
import json
import urllib.parse

# https://github.com/kotofurumiya/pokemon_data
with open('./pokemon_data.json', 'r', encoding='utf-8') as f:
    pokemon_list = json.load(f)

poke_scraped_data = []
for poke_info in pokemon_list:
    print('extracting... '+poke_info['name'])
    resp = requests.get('http://pokemon-wiki.net/'+ urllib.parse.quote(poke_info['name']), timeout=1)
    soup = BeautifulSoup(resp.text, features="html.parser")
    content = soup.find("h2", id="content_1_0")
    if content is None:
        continue
    hr_count = 0
    poke_data = {
        'no':poke_info['no'],
        'name':poke_info['name'],
        'desc':''
    }
    for sib in content.next_siblings:
        if sib.name == 'hr':
            hr_count+=1

        # 2個目のhr~3個目のhrまでが概要
        if hr_count == 2 and sib.name == 'p':
            poke_data['desc'] += sib.text

    poke_scraped_data.append(poke_data)

with open('./data/pokemon_scraped_data.json', 'w', encoding='utf-8') as f:
    pokemon_list = json.dump(poke_scraped_data, f,ensure_ascii=False)
