from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import posts

# Create your views here.

@api_view(['GET'])
def get_posts(request):
    post_list = posts.posts
    return Response(post_list)

@api_view(['GET'])
def get_post(request, pk):
    post = [post for post in posts.posts if str(post['_id']) == pk]
    if post:
        return Response(post[0])
    return Response(None)
