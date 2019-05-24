from rest_framework import routers
from django.urls import path
from pokemon.views import SearchSimilarStatsView, FuzzyTermSearchView, SearchSimilarDescView

urlpatterns = [
    path(r'api/pokemon/similarStats', SearchSimilarStatsView.as_view()),
    path(r'api/pokemon/fuzzyTerm', FuzzyTermSearchView.as_view()),
    path(r'api/pokemon/similarDesc', SearchSimilarDescView.as_view()),
]
