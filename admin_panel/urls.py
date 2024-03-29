from django.urls import path, include
from .views import *
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'category', CategoryView)

urlpatterns = [
    path('', include(router.urls)),

    path('userslist/',UsersList.as_view(), name='users-list'),
    path('user-block/<int:pk>/',UserBlock.as_view(),name='block-user'),
    path('user-unblock/<int:pk>/',UserUnblock.as_view(),name='unblock-user'),

    path('register-expert/',ExpertRegister.as_view(),name='register-expert'),
    path('edit-expert/<int:pk>/',ExpertEdit.as_view(),name='edit-expert'),
    path('expert-list/',ExpertList.as_view(),name='expert-list'),
    path('expert-block/<int:pk>/',ExpertBlock.as_view(),name='block-expert'),
    path('expert-unblock/<int:pk>/',ExpertUnblock.as_view(),name='expert-unblock'),

    path('issues/<int:user_id>/<int:expert_id>/',IssuesRegister.as_view(),name='register-issues'),
    path('issues-list/',IssuesList.as_view(),name='issues-list'),
    
    path('expert-category/',Category_Expert_Filter.as_view(),name='category-expert-filter'),

    path('last-login-list/',LastLoginUserlist.as_view(),name='category-expert-filter'),
    
]
