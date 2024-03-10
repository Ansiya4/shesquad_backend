from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import UpdateAPIView, ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import *
from django.db.models import Q
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
    queryset = CustomUser.objects.all()


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


class IssuesRegister(CreateAPIView):
    serializer_class = IssuesRegistrationSerializer
    def post(self, request, user_id, expert_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            expert = CustomUser.objects.get(id=expert_id)
        except CustomUser.DoesNotExist:
            return Response("User or expert not found", status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user, expert=expert)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    

class IssuesList(ListAPIView):
    queryset = Issues.objects.all()
    serializer_class = IssueListSerializer


class Category_Expert_Filter(ListAPIView):
    serializer_class = UserListSerializer
    queryset = CustomUser.objects.all()

    def get_queryset(self):
            cat_id = self.request.query_params.get('cat_id')
            queryset = CustomUser.objects.exclude(Q(is_superuser=True) | Q(category__isnull=True) )

            if cat_id:
                queryset = queryset.filter(category=cat_id)

            return queryset



# Dashboard Home user lastLogin List
class LastLoginUserlist(ListAPIView):
    serializer_class = UserListSerializer
    queryset = CustomUser.objects.all()[:5]