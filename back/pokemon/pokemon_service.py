import os
import json
import MeCab
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, "data/pokemon_scraped_data.json"), encoding="utf-8") as f:
    pokemon_scraped_data = json.load(f)

with open(os.path.join(base_dir, "data/pokemon_data.json"), encoding="utf-8") as f:
    pokemon_data = json.load(f)

no_to_pokedata_dict = {data['no']: data for data in pokemon_data}
stats_keys = ['hp', 'attack', 'defence', 'spAttack', 'spDefence', 'speed']
stats_all = [[data['stats'][key] for key in stats_keys] for data in pokemon_data]

tagger = MeCab.Tagger(r"-Owakati")

wakati_arr = []
for data in pokemon_scraped_data:
    parsed = tagger.parse(data['desc'])
    wakati_arr.append(parsed)

# デフォルトのtoken_patternは1文字の単語を無視するので、無視しないようにする
TOKEN_PATTERN = u'(?u)\\b\\w+\\b'
vectorizer = TfidfVectorizer(token_pattern=TOKEN_PATTERN)
x_all = vectorizer.fit_transform(wakati_arr)


def fuzzyTermSearch(terms: str):
    x = vectorizer(tagger.parse(terms))
    similarities = cosine_similarity([x], x_all)[0]

    found = []
    # 類似度昇順に並び替え、上位10件を抽出
    top_indices = np.argsort(similarity)[::-1][:10]
    for index in top_indices:
        no = pokemon_scraped_data[index]['no']
        found.append(no_to_pokedata_dict[no])

    return found

def searchSimilarStats(argStats):
    stats = [int(argStats[key]) for key in stats_keys]
    print(stats)
    similarities = cosine_similarity([stats], stats_all)[0]
    # 類似度昇順に並び替え、上位10件を抽出
    top_indices = np.argsort(similarities)[::-1][:10]
    found = []
    for index in top_indices:
        no = pokemon_data[index]['no']
        found.append(no_to_pokedata_dict[no])
    return found
