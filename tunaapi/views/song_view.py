from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Artist, Genre


class SongView(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            song = Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

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


class SongArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name', )


class SongGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'description', )

class SongSerializer(serializers.ModelSerializer):
    artist = SongArtistSerializer(many=False)
    genre = SongGenreSerializer(many=False)

    class Meta:
        model = Song
        fields = ('id', 'artist', 'genre', 'length', 'album', 'title',)
