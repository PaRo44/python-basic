from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def cv(request):
    return render(request, 'website/cv.html')


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    return render(request, 'website/contacts.html')


def blog(request):
    return render(request, 'website/blog.html')
