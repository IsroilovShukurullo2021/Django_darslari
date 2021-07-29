from django.shortcuts import render
from django.http import HttpResponse  # bu javob qaytaradigan kutubxona moduli

# Create your views here.
def hello (request):
    return HttpResponse("<font color='red'><h1><i>Salom</i> yoshlar</h1></font>")

def goodbye(request):
    return HttpResponse("Hayr")

def ism(request):
    return HttpResponse("<h3>Isroilov Shukurullo</h3>")
def sahifa(request):
    name='Shukurullo'
    names=['Umida','Dilbar','Shodiyona','Muslima']
    avtomobel=' matiz'
    return render(request,'index.html',{'ism':name,'ismlar':names})