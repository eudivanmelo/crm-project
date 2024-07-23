from django.urls import path
from .views.auth import LoginView, RegisterView
from .views.category import Category_ListView, Category_CreateView, Category_UpdateView, Category_DeleteView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_page'),
    path('register/', RegisterView.as_view(), name='register_page'),

    path('categories/', Category_ListView.as_view(), name='category-list'),
    path('category/create/', Category_CreateView.as_view(), name='category-create'),
    path('category/edit/<int:pk>/', Category_UpdateView.as_view(), name='category-update'),
    path('category/delete/<int:pk>/', Category_DeleteView.as_view(), name='category-delete')
]