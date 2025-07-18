from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate,login

# create a serializer for Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','state','city','country','image']

# create a serializer for category 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# create a serializer for post 
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

        
# create a serializer for login
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return user
        else:
            raise serializers.ValidationError("No user found with this username or password")

    

# create a serializer for User signUp
class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','email','password','state','city','country','image']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            state=validated_data['state'],
            city=validated_data['city'],
            country=validated_data['country'],
            image=validated_data['image']
        )
        return user