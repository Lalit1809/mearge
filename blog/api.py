from rest_framework.permissions import IsAuthenticated
from rest_framework import status , viewsets 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializers import *
from .models import *

# create a api for comments using a ModelViewSets
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
# create a api for tags using a ModelViewStes
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# create a api for Profile using ModelViewStes
class ProfileViewSte(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only the profile of the logged-in user
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        # Force every action to return only the logged-in user object
        return self.request.user
   


# create a api for category using a ModelViewSets
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# create a api for post using a ModelViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# create a api for login using genric
class UserLoginView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        print('inside login apiiiiiiiiiiii')
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data,'nnnnnnnnnnnnn')
        user = serializer.validated_data
        print(user,'>>>>>>>>>>>>>>>>')
        # Log in the user (if not already handled in the serializer)
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        return Response({'message': 'Login successful','token': token.key,}, status=status.HTTP_200_OK)



# create a api for user signup using genric 

class UserRegistrationView(CreateAPIView):
    querySet = User.objects.all()
    serializer_class = UserRegistrationSerializer
    

# create a api for user signup using APIView 

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        print(serializer,'ssssssssssssssssssssssssssssssssssss')
        if serializer.is_valid():
            serializer.save()
            return Response({
              "message": "User registered successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
