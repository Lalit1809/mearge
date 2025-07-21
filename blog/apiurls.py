from django.urls import path,include
from . import views
from .api import *
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from blog.api import *
router = DefaultRouter()
router.register(r'posts', PostViewSet,basename='post')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'profile', ProfileViewSte,basename='profile')
router.register(r'tag',TagViewSet,basename='tag')
router.register(r'comment',CommentViewSet,basename='comment')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),

]