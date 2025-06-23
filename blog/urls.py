from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post-new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # create a new urls for sign-up page
    path('signup/', views.sign_up, name='sign_up'),
    # create a new urls for login page
    path('login/', views.login_page, name='login'),
    # create a new urls for sign_out page
    path('logout/',views.sign_out,name='sign_out'),
    # create a bew urls for profile page
    path('profile/',views.profile_page,name='profile'),
    # cerate a new urls for edit page
    path('edit/',views.edit_page,name='edit'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)