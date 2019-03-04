from rest_framework import viewsets

from cineclub.apps.film.models import Film
from cineclub.apps.film.serializers import FilmSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
