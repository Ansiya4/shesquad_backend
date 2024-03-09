from rest_framework import serializers
from .models import *
from accounts.models import CustomUser



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password',)


class ExpertRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name','last_name','email','password','category','profile_picture','description']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

