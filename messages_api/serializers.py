from rest_framework import serializers

import messages_api.models


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = messages_api.models.Message
        fields = ['subject', 'body']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = messages_api.models.Post
        fields = '__all__'
