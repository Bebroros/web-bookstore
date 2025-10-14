from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True, max_length=32)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())], max_length=32)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'password2']
        extra_kwargs = {
                        'password': {'write_only': True, 'min_length': 8, 'max_length': 32},
                        'first_name': {'required': False, 'max_length': 32},
                        'last_name': {'required': False, 'max_length': 32},
                        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Passwords must match.')
        return attrs

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        extra_kwargs = {
                        'password': {'write_only': True, 'min_length': 8, 'max_length': 32},
                        'first_name': {'required': False, 'max_length': 32},
                        'last_name': {'required': False, 'max_length': 32},
                        }


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['is_staff'] = user.is_staff
        return token
