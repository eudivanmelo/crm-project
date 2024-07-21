from django.urls import path
from .views.auth import LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_page'),
    path('register/', RegisterView.as_view(), name='register_page'),
]