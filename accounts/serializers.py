from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import *
from admin_panel.serializers import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name', 'last_name','email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
        
class UserEditSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'profile_picture', 'email','category']



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['category'] = user.category.id if user.category else ''
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['is_admin'] = user.is_superuser
        return token



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


