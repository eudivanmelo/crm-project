from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from main_app.models import StockItem
from ..serializers import StockItemSerializer
from ..permissions import CustomDjangoModelPermission

class StockItemListCreate_APIView(generics.ListCreateAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockItemSerializer
    permission_classes = [IsAuthenticated, CustomDjangoModelPermission]

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class StockItemRetrieveUpdateDestroy_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockItemSerializer
    permission_classes = [IsAuthenticated, CustomDjangoModelPermission]
