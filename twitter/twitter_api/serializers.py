from rest_framework import serializers

from .models import *


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = ("name", "text", "timestamp")
