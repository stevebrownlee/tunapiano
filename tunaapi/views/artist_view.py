from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Artist


class ArtistView(ViewSet):

    def retrieve(self, request, pk=None):
        artist = Artist.objects.get(pk=pk)
        serialized = ArtistSerializer(artist, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        artists = Artist.objects.all()
        serialized = ArtistSerializer(artists, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        artist = Artist.objects.create(
            name=request.data['name'],
            age=request.data['age'],
            bio=request.data['bio'],
        )
        artist.save()

        serialized = ArtistSerializer(artist, many=False)
        return Response(serialized.data, status=status.HTTP_201_CREATED)


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'bio', 'age', 'name', )
