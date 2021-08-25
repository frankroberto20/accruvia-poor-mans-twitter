import json
from .serializers import *
from rest_framework import viewsets
from django.http.response import JsonResponse
from twitter_api.models import Tweet
from django.http.request import HttpRequest

# Create your views here.


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by("-timestamp")
    serializer_class = TweetSerializer
