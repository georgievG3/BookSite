from django.shortcuts import render
from books.models import Book

# Create your views here.
def book_list(request):
    books = Book.objects.filter(genre__name='Best Books')
    crime_books = Book.objects.filter(genre__name='Crime')
    fantasy_books = Book.objects.filter(genre__name='Fantasy')
    return render(request, 'books/index.html', {
        'books': books,
        'crime_books': crime_books,
        'fantasy_books': fantasy_books,
    })