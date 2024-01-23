from django.shortcuts import render
from .serializer import AuthorSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Author
# Create your views here.

class AuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorById(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer