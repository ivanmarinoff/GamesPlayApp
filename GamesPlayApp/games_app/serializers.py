from rest_framework import serializers
from .models import Game, Profile


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['title', 'category', 'rating']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password', 'first_name', 'last_name', 'profile_picture']
