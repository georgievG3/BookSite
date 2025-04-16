from django.db.models import Q
from django.shortcuts import render, redirect
from books.models import Book
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("my-login")

    context = {'registerform': form}

    return  render(request, 'books/register.html', context = context)



def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {'loginform': form}

    return  render(request, 'books/my-login.html', context=context)

@login_required(login_url="my-login")
def dashboard(request):
    return render(request, 'books/dashboard.html')

def user_logout(request):
    auth.logout(request)

    return redirect('book_list')
