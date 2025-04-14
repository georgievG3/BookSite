from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('search_results', views.search_results, name='search-results'),

]