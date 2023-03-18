from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerialzer

# using ListCreateAPIView, Read & Write Operations


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialzer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
