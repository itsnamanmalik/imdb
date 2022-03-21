import imp
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from bs4 import BeautifulSoup
import requests
import re
from api.models import *
from api.serializers import MovieSerializer
from django.shortcuts import render
from django.views import View
from django.db.models import Q


class Index(View):
    def get(self, request):
        return render(request,'index.html')
 

class FetchTopMovies(APIView):
    def get(self, request):
        url = 'http://www.imdb.com/chart/top'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        
        movies = soup.select('td.titleColumn')
        ratings = [b.attrs.get('data-value')
                for b in soup.select('td.posterColumn span[name=ir]')]    
        Movie.objects.all().delete()
        for index in range(0, 50):
            movie_string = movies[index].get_text()
            movie = (' '.join(movie_string.split()).replace('.', ''))
            movie_title = movie[len(str(index))+1:-7]
            year = re.search('\((.*?)\)', movie_string).group(1)
            movi = Movie(name=movie_title,year=year,rating=ratings[index])
            movi.save()
        return Response({'message':'All Top 50 Movies Fetched & Stored in Database'}, status=status.HTTP_200_OK)
    
    
class MoviesApi(APIView):
    def get(self, request):
        all_movies = Movie.objects.all()
        serializer = MovieSerializer(all_movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

class SearchMovies(APIView):
    def get(self, request):
        name = request.GET.get('name')
        year = request.GET.get('year')
        if name and not year:
            all_movies = Movie.objects.filter(Q(name__icontains=name))
        elif not name and year:
            all_movies = Movie.objects.filter(year=year)
        elif name and year:
            all_movies = Movie.objects.filter(name=name, year=year)
        else:
            return Response({'message':'No query found name or year'},status=status.HTTP_400_BAD_REQUEST)
        serializer = MovieSerializer(all_movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    