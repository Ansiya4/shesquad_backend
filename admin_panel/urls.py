from django.urls import path
from .views import *


urlpatterns = [
    path('add-category/', CategoryCreateView.as_view(), name='add-category'),
    path('category-list/', CategoryRetrieveView.as_view(), name='category-list'),
    path('edit-category/<int:pk>/',CategoryEditView.as_view(), name='edit-category'),
]
