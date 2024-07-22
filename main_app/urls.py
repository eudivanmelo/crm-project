from django.urls import path
from .views.auth import LoginView, RegisterView
from .views.category import Category_ListView, Category_CreateView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_page'),
    path('register/', RegisterView.as_view(), name='register_page'),

    path('categories/', Category_ListView.as_view(), name='category-list'),
    path('category/create', Category_CreateView.as_view(), name='category-create')
]