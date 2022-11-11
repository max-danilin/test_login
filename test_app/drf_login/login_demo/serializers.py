from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token

    def validate(self, data):
        credentials = {
            'username': '',
            'password': data.get("password")
        }
        user_obj = get_user_model().objects.filter(email=data.get("username")).first() or get_user_model().objects.filter(username=data.get("username")).first()
        if user_obj:
            credentials['username'] = user_obj.username
        return super().validate(credentials)


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError('Passwords must match!')
        return data

    def validate_username(self, data):
        query = get_user_model().objects.filter(username__iexact=data)
        if query.exists():
            raise serializers.ValidationError('User with this username already exists!')
        return data

    def validate_email(self, data):
        query = get_user_model().objects.filter(email__iexact=data)
        if query.exists():
            raise serializers.ValidationError('User with this email already exists!')
        return data

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )     
        user.set_password(validated_data['password'])
        user.save()
        return user
