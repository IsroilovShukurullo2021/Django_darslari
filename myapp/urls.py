from django.urls import path
from .import views
urlpatterns =[
    path('',views.hello),

    path('maktab/',views.goodbye),

    path('ism/',views.ism),

    path('sahifa/',views.sahifa),

]