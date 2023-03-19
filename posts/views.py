from django.shortcuts import render
from rest_framework import generics, permissions  ######Do not for get it
from .models import Post
from .serializers import PostSerialzer
from .permissions import IsAuthorOrReadOnly

# using ListCreateAPIView, Read & Write Operations


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    # unauthorized users can view any page, but only authenticated users have write, edit, or delete privileg
    queryset = Post.objects.all()
    serializer_class = PostSerialzer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthorOrReadOnly,
    )  # if you forget the comma you will get an error : Django REST Framework: 'BasePermissionMetaclass' object is not iterable
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
