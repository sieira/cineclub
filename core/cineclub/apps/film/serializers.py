from rest_framework import serializers

from cineclub.apps.film.models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('pk', 'name')
