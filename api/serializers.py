from rest_framework import serializers
from main_app.models import Category, Product, StockItem
from django.contrib.auth.models import User, Group

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = User
        fields = ('first_name', 'username', 'password', 'email')
    
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name = validated_data.get('first_name', ''),
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data.get('email', '')
        )

        try:
            group = Group.objects.get(name='operator')
            user.groups.add(group)
        except Group.DoesNotExist:
            print("Error adding group to user in 'api-register'")

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'email']

class CategorySerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_by']

class ProductSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    category_detail = CategorySerializer(source='category', read_only=True)  # Para leitura

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_by']

class StockItemSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = StockItem
        fields = '__all__'
        read_only_fields = ['created_by']