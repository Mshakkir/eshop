from django.urls import path
from . import views

app_name='search_app'
urlpatterns=[
    path('', views.SearchForm, name='SearchForm'),
    path('result/', views.SearchResult, name='SearchResult'),
]
