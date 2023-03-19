from django.shortcuts import render
from rest_framework import generics, permissions  ######Do not for get it
from .models import Post
from .serializers import PostSerialzer

# using ListCreateAPIView, Read & Write Operations


class PostList(generics.ListCreateAPIView):
    # unauthorized users can view any page, but only authenticated users have write, edit, or delete privileg
    queryset = Post.objects.all()
    serializer_class = PostSerialzer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
