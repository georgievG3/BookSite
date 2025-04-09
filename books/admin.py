from django.contrib import admin
from books.models import Book, Genre

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre', 'author', 'cover_image', 'description', 'rating']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

