from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..serializers import CategorySerializer
from main_app.models import Category
from ..permissions import CustomDjangoModelPermission

class CategoryListCreate_APIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, CustomDjangoModelPermission]

    def get_permissions(self):
        return [permission() for permission in self.permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CategoryRetrieveUpdateDestroy_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, CustomDjangoModelPermission]

    def get_permissions(self):
        return [permission() for permission in self.permission_classes]