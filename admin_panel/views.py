from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class CategoryCreateView(CreateAPIView):
    serializer_class = CategorySerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response({'message' : 'Category added successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryRetrieveView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryEditView(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = self.get_serializer(category)
        data = serializer.data
        return Response(data)