from rest_framework import routers
from django.urls import path
from pokemon.views import SearchSimilarStatsView, FuzzyTermSearchView

router = routers.SimpleRouter()
router.register(r'api/pokemon/similarStats', SearchSimilarStatsView.as_view())
router.register(r'api/pokemon/fuzzyTerm', FuzzyTermSearchView.as_view())
urlpatterns = router.urls
