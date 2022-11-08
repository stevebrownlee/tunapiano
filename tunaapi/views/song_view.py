from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Artist, Genre


class SongView(ViewSet):

    def retrieve(self, request, pk=None):
        song = Song.objects.get(pk=pk)
        serialized = SongSerializer(song)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        songs = Song.objects.all()
        serialized = SongSerializer(songs, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        song = Song.objects.create(
            artist=Artist.objects.get(pk=request.data['artistId']),
            genre=Genre.objects.get(pk=request.data['genreId']),
            length=request.data['length'],
            album=request.data['album'],
            title=request.data['title'],
        )
        song.save()

        serialized = SongSerializer(song)
        return Response(serialized.data, status=status.HTTP_201_CREATED)


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('id', 'artist', 'genre', 'length', 'album', 'title',)
