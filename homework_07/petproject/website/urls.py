from django.urls import path

from . import views

#app_name = 'website'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('cv/', views.cv, name='cv'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
