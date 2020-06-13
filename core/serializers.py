from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import Product

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate(self, data, *args, **kwargs):
        return super(UserCreateSerializer, self).validate(data, *args, **kwargs)
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user

    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'username')


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'rating')
