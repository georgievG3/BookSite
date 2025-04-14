from django.db.models import Q
from django.shortcuts import render
from books.models import Book
from django.http import JsonResponse

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

def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        query = Q(name__icontains=searched) | Q(author__icontains=searched)
        books_results = Book.objects.filter(query)
        return render(request, 'books/search-results.html', {'searched': searched, "books_results": books_results})
    else:
        return render(request, 'books/search-results.html', {})