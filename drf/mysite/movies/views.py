from django.shortcuts import render
from rest_framework import viewsets #needed to inherit with class
from .serializers import MovieSerializer
from .models import Moviedata
# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='Action')
    serializer_class = MovieSerializer

class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ = 'Thriller')
    serializer_class = MovieSerializer

class DramaViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='Drama')
    serializer_class = MovieSerializer