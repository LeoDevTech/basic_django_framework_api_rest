from django.urls import path
from .views import book_list, book_search
urlpatterns = [
    path('', book_list, name='book-list'),
    path('<int:pk>', book_search, name='book-search')
]
