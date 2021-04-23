from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def get_posts(request):
    return Response('Blog Posts')

@api_view(['GET'])
def get_post(request, pk):
    post = None
    return Response(post)
