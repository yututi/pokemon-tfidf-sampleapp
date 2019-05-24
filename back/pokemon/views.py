from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .pokemon_service import fuzzyTermSearch, searchSimilarStats, search_similar_poke

class FuzzyTermSearchView(APIView):
    def get(self, req):
        query_string = req.GET['query']
        pokemons = fuzzyTermSearch(query_string)
        return Response(pokemons)

class SearchSimilarStatsView(APIView):
    def get(self, req):
        pokemons = searchSimilarStats(req.GET)
        return Response(pokemons)

class SearchSimilarDescView(APIView):
    def get(self, req):
        no = req.GET['no']
        pokemons = search_similar_poke(no)
        return Response(pokemons)