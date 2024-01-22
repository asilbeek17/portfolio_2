from django.urls import path
from app.views import index, single, registerPage, loginPage, posts, custom_logout

urlpatterns = [
    path('', index, name='index'),
    path('single/<int:id>/', single, name='single'),
    path('posts/', posts, name='posts'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('acounts/logout/', custom_logout, name='logout')
]
