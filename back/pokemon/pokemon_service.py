import os
import json
import MeCab
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# データ準備
base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, "data/pokemon_scraped_data.json"), encoding="utf-8") as f:
    pokemon_scraped_data = json.load(f)

with open(os.path.join(base_dir, "data/pokemon_data.json"), encoding="utf-8") as f:
    pokemon_data = json.load(f)

no_to_pokedata_dict = {data['no']: data for data in pokemon_data}
no_to_pokedesc_dict = {data['no']: data for data in pokemon_scraped_data}
stats_keys = ['hp', 'attack', 'defence', 'spAttack', 'spDefence', 'speed']
stats_all = [[data['stats'][key] for key in stats_keys] for data in pokemon_data]

# 分かち書き
tagger = MeCab.Tagger(r"-Owakati")
tagger.parse('')

wakati_arr = []
for data in pokemon_scraped_data:
    parsed = tagger.parse(data['desc'])
    wakati_arr.append(parsed)

# デフォルトのtoken_patternは1文字の単語を無視するので、無視しないようにする
vectorizer = TfidfVectorizer(token_pattern=u'(?u)\\b\\w+\\b')
x_all = vectorizer.fit_transform(wakati_arr)

def fuzzyTermSearch(terms: str):
    """
        あいまい単語検索
        Parameters
        ----------
        terms : str
            単語
        Returns
        -------
        単語に類似するポケモンのリスト
    """
    x = vectorizer.transform([tagger.parse(terms)])  # TODO: モデル構築済みのVectorizerはスレッドセーフ？
    similarities = cosine_similarity(x, x_all)[0]

    found = []
    # 類似度降順に並び替え、上位10件を抽出
    top_indices = np.argsort(similarities)[::-1][:10]
    for index in top_indices:
        if(similarities[index] > 0):
            no = pokemon_scraped_data[index]['no']
            found.append(no_to_pokedata_dict[no])

    return found

def searchSimilarStats(argStats):
    """
    種族値類似検索
    Parameters
    ----------
    argStats : array of int
        種族値の配列(HP、こうげき、防御、とくこう、とくぼう、すばやさの順)
    Returns
    -------
    引数の種族値に類似するポケモンのリスト
    """

    stats = [int(argStats[key]) for key in stats_keys]
    similarities = cosine_similarity([stats], stats_all)[0]
    # 類似度降順に並び替え、上位10件を抽出
    top_indices = np.argsort(similarities)[::-1][:10]
    found = []
    for index in top_indices:
        no = pokemon_data[index]['no']
        found.append(no_to_pokedata_dict[no])
    return found

def search_similar_poke(no:int):
    """
    """
    desc = no_to_pokedesc_dict[no]["desc"]
    return fuzzyTermSearch(desc)