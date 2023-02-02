from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post


def index(request):
    return render(request, 'website/index.html')


def cv(request):
    return render(request, 'website/cv.html')


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    return render(request, 'website/contacts.html')


class PostListView(ListView):
    model = Post
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
