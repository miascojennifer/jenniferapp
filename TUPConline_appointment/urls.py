
from django.urls import path
from . import views

urlpatterns = [
	path('', views.loginPage, name='login'),
	path('login/', views.loginPage, name='login'),
	path('register/', views.registerPage, name='register'),
	path('main/', views.Main, name='main'),
	path('make/', views.make, name='make'),
	path('home/', views.home, name='home'),
	path('dhome/', views.depthome, name='dhome'),	
	path('update/<str:pk>/', views.update, name="update"),
	path('logout/', views.logoutUser, name="logout"),
	]