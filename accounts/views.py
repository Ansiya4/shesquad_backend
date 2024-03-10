from django.shortcuts import render
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegister(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = CustomUser.objects.all()
    

class UserEdit(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserEditSerializer
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        data = serializer.data
        return Response(data)
