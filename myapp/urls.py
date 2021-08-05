from django.urls import path
from .import views
urlpatterns =[
    path('',views.hello, name='index'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('login/praktika/',views.praktika, name='praktika'),
    path('logout/',views.logout,name='logout')


]