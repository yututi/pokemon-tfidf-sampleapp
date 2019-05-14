from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .pokemon_service import fuzzyTermSearch, searchSimilarStats

class FuzzyTermSearchView(APIView):
    def get(self, req):
        query_string = req.GET['query']
        pokemons = fuzzyTermSearch(query_string)
        return Response(pokemons)

class SearchSimilarStatsView(APIView):
    def get(self, req):
        pokemons = searchSimilarStats(req.GET)
        return Response(pokemons)
