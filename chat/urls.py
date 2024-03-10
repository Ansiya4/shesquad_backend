from django.urls import path
from .views import *
urlpatterns = [
    path('userlisting/<int:id>/', UserListing.as_view(), name='UserListing'),
    path("user-previous-chats/<int:user1>/<int:user2>/", PreviousMessagesView.as_view()),

    path("addtochat/", AddToChat.as_view()),
    path("addtochat-user-list/<int:user_id>", AddToChatListUserSide.as_view()),
    path("addtochat-expert-list/<int:expert_id>", AddToChatListExpertsSide.as_view()),

]


