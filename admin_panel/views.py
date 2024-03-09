from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import UpdateAPIView, ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserRegistrationSerializer
# Create your views here.

class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class UsersList(ListAPIView):
    serializer_class = UserListSerializer
    queryset = CustomUser.objects.filter(category__isnull=True).exclude(is_staff=True)


class UserBlock(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({'message' : 'User blocked successfully'}, status= status.HTTP_200_OK)


class UserUnblock(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = True
        user.save()
        return Response({'message':'Unblocked successfully'},status=status.HTTP_200_OK)


class ExpertRegister(CreateAPIView):
    serializer_class = ExpertRegistrationSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message' : 'Registration successfully completed'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ExpertEdit(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ExpertRegistrationSerializer
    def get(self, request, *args, **kwargs):
        expert = self.get_object()
        serializer = self.get_serializer(expert)
        data = serializer.data
        return Response(data)
    

class ExpertList(ListAPIView):
    serializer_class = UserListSerializer
    queryset = CustomUser.objects.filter(category__isnull=False).exclude(is_staff=True)


class ExpertBlock(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ExpertRegistrationSerializer
    def update(self, request, *args, **kwargs):
        expert = self.get_object()
        expert.is_active = False
        expert.save()
        return Response({'message':'Expert has been blocked successfully'},status=status.HTTP_200_OK)


class ExpertUnblock(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ExpertRegistrationSerializer
    def update(self, request, *args, **kwargs):
        expert = self.get_object()
        expert.is_active = True
        expert.save()
        return Response({'message' : 'Expert has been unblocked successfully'},status=status.HTTP_400_BAD_REQUEST)
