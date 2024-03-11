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
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'category', 'profile_picture', 'description']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(password=password, **validated_data)
        return user

class IssuesRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = ['message']


class IssueListSerializer(serializers.ModelSerializer):
    user_firstname = serializers.SerializerMethodField()
    expert_firstname = serializers.SerializerMethodField()

    class Meta:
        model = Issues
        fields = ['user_firstname', 'expert_firstname', 'message']

    def get_user_firstname(self, obj):
        return obj.user.first_name if obj.user else None

    def get_expert_firstname(self, obj):
        return obj.expert.first_name if obj.expert else None
