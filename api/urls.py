from django.urls import path,include
from api.views import *


urlpatterns = [
    
     path('',Index.as_view()),
     path('fetchmovies',FetchTopMovies.as_view()),
     path('moviesapi',MoviesApi.as_view()),
     path('searchmovie',SearchMovies.as_view()),
     
]