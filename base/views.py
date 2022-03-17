from django.shortcuts import render
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.postgres.search import TrigramSimilarity
from .serializers import *


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True, methods=["GET"])
    def albums(self, request, pk, *args, **kwargs):
        author = Author.objects.get(id=pk)
        album = Album.objects.filter(author=author)
        serializer = AlbumSerializer(album, many=True)
        return Response(serializer.data)
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,]
    ordering_fields = ["age",]
    search_fields = ["name","id","count","track",]

    # def get_queryset(self, request):
    #     word = self.get_params("search")
    #     if word is not None:
    #         music = Music.objects.annotate(
    #             similarity=TrigramSimilarity("name",word)
    #         ).filter(similarity__gt=0.5)
    #     serializer = MusicSerializer(music)
    #     return Response(serializer.data)


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    @action(detail=True, methods=["GET","POST"])
    def author(self, request, pk):
        album = Album.objects.get(id=pk)
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            a = Author.objects.last()
            album.author.add(a)
            album.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    filter_backends = [filters.OrderingFilter,]
    ordering_fields = ["year",]

class MusicViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    def retrieve(self, request,pk=None, *args, **kwargs):
        queryset = Music.objects.all()
        music = get_object_or_404(queryset, pk=pk)
        music.listened += 1
        music.save()
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,]
    ordering_fields = ["listened","name","duration","year",]
    search_fields = ["id","name","year","duration",]

