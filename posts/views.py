from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets  ######Do not for get it
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAdminUser

# New implementation of viewsets for DRY code


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# using ListCreateAPIView, Read & Write Operations


# class PostList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     # unauthorized users can view any page, but only authenticated users have write, edit, or delete privileg
#     queryset = Post.objects.all()
#     serializer_class = PostSerialzer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (
#         IsAuthorOrReadOnly,
#     )  # if you forget the comma you will get an error : Django REST Framework: 'BasePermissionMetaclass' object is not iterable
#     queryset = Post.objects.all()
#     serializer_class = PostSerialzer


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
