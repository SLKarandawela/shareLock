from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from passlib.hash import sha256_crypt as sha256
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from messages_api.models import Post
from messages_api.serializers import MessageSerializer, PostSerializer


# Create your views here.
class CreateMessage(generics.CreateAPIView):
    serializer_class = MessageSerializer

    def post(self, request):
        print(request.data)
        subject = sha256.encrypt(request.data.get('subject'), rounds=5000)
        body = sha256.encrypt(request.data.get('body'), rounds=5000)
        print("subject, body", subject, body)
        hashed_dict = {
            'subject': subject,
            'body': body
        }
        create_serializer = self.serializer_class(data=hashed_dict)
        if create_serializer.is_valid():
            create_serializer.save()
            return Response(create_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PostView(generics.CreateAPIView):

    @csrf_exempt
    def post(self, request):
        print(request.data)
        title = request.data.get('title')
        content = request.data.get('content')
        image = sha256.encrypt(request.data.get('image'), rounds=5000)

        print("subject, body", title, content, image)
        hashed_dict = {
            'title': title,
            'content': content,
            'image': image
        }
        posts_serializer = PostSerializer(data=hashed_dict)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
