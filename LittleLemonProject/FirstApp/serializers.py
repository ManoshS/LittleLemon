from rest_framework import serializers
from .models import Menu ,Booking
from django.contrib.auth.models import User
class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

        def create(self,validated_data):
            user=User.objects.create(username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
            return user

    