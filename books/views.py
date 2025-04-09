from django.shortcuts import render
from books.models import Book

# Create your views here.
def add_book(request):
    return render(request, 'books/add_book.html')

def book_list(request):
    books = Book.objects.filter(genre__name = 'Best Books')
    return render(request, 'books/index.html', {'books': books})