from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Post.objects.all()

class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Post.objects.all()