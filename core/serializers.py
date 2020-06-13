from django.contrib.auth.models import User
from rest_framework import serializers

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate(self, data, *args, **kwargs):
        return super(UserCreateSerializer, self).validate(data, *args, **kwargs)

    
    def create(self, validated_data):

        # first_name = validated_data['first_name']
        # last_name = validated_data['last_name']
        # email = validated_data['email']
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user

    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'username')
