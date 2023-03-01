from django.urls import path

from . import views

#app_name = 'website'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('cv/', views.cv, name='cv'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.PostListView.as_view(), name='post-list'),
    path('blog/<int:pk>', views.PostDetailView.as_view(), name='post')
]
