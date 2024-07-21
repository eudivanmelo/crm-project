from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from main_app.models import Product
from ..serializers import ProductSerializer
from ..permissions import CustomDjangoModelPermission

class ProductListCreate_APIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, CustomDjangoModelPermission]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductRetrieveUpdateDestroy_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, CustomDjangoModelPermission]