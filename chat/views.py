from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.filters import SearchFilter
from .serializers import *
from accounts.models import *
from .models import *
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

class UserListing(ListAPIView):
    serializer_class = UserListserializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name','last_name','email']
    # permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user_id = self.kwargs['id']
        queryset = CustomUser.objects.all().exclude(Q(id=user_id) | Q(is_superuser=True))
        return queryset
    
class ExpertsListing(ListAPIView):
    serializer_class = UserListserializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name','last_name','email']
    # permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user_id = self.kwargs['id']
        queryset = CustomUser.objects.all().exclude(Q(id=user_id) | Q(is_superuser=True))
        return queryset

class PreviousMessagesView(ListAPIView):
    serializer_class = MessageSerializer
    pagination_class = None
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user1 = int(self.kwargs['user1'])
        user2 = int(self.kwargs['user2'])

        thread_suffix = f"{user1}_{user2}" if user1 > user2 else f"{user2}_{user1}"
        thread_name = 'chat_'+thread_suffix
        queryset = Message.objects.filter(
            thread_name=thread_name
        )
        return queryset
    
class AddToChat(CreateAPIView):
    queryset = ChatList.objects.all()
    serializer_class = ChatSerializer
    
class AddToChatListUserSide(ListAPIView):
    queryset = ChatList.objects.all()
    serializer_class = ChatListSerializer

    def get_queryset(self):
        user_id = int(self.kwargs['user_id'])
        queryset = ChatList.objects.filter(user=user_id)
        return queryset


class AddToChatListExpertsSide(ListAPIView):
    queryset = ChatList.objects.all()
    serializer_class = ChatListSerializer

    def get_queryset(self):
        expert_id = int(self.kwargs['expert_id'])
        queryset = ChatList.objects.filter(expert=expert_id)
        return queryset