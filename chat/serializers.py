from rest_framework.serializers import ModelSerializer
from .models import Message
from accounts.models import *
from rest_framework import serializers
from .models import *
class UserListserializer(serializers.ModelSerializer):
   class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name','last_name', 'profile_picture']

class MessageSerializer(ModelSerializer):
    sender_email = serializers.EmailField(source='sender.email')

    class Meta:
        model = Message
        fields = ['message', 'sender_email']

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatList
        fields = '__all__'  

class ChatListSerializer(serializers.ModelSerializer):
    user = UserListserializer()
    expert = UserListserializer()
    class Meta:
        model = ChatList
        fields = '__all__'  