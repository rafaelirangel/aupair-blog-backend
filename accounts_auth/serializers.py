from rest_framework import serializers
from .models import UserAccount
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


#User Register Serializer
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserAccount.objects.create_user(
            password=password, **validated_data)
        return user

#Obtain Token Serializer, User Login
class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['email'] = self.user.email
        data['name'] = self.user.name

        return data
