from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/index.html')


def aboutus(request):
    return render(request, 'home/aboutus.html')


def notice(request):
    return render(request, 'home/notice.html')


def colleges(request):
    return render(request, 'home/colleges.html')


def program(request):
    return render(request, 'home/program.html')


def download(request):
    return render(request, 'home/download.html')
