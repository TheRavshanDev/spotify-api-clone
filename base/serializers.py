from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Album, Author, Music
from rest_framework.exceptions import APIException

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
    
    def validate_photo(self, value):
        if value[-1: -5] != ".png" or value[-1:-5] != ".jpg":
            raise APIException("Rasm formati png yoki jpg bo'lishi kerak")
        return value

    # def validate_photo(self, value):
    #     if ".png" in value or ".jpg" in value:
    #         return value
    #     raise APIException("Rasm formati png yoki jpg bo'lishi kerak!")

class MusicSerializer(ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'

    def validate_music(self, value):
        if value[-1: -5] != ".mp3" or value[-1:-5] != ".mp4":
            raise APIException("Qo'shiq formati mp3 yoki mp4 bo'lishi kerak")
        return value
    # def validate_music(self, value):
    #     if ".mp3" in value:
    #         print(value)
    #         return value
    #     raise APIException("Qo'shiq formati .mp3 bo'lishi kerak")
