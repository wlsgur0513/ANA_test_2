from django.shortcuts import render



def index(request): return render(request, 'mainpage.html')

def file(request): return render(request, 'img_upload.html')