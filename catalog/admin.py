from django.contrib import admin

# Register your models here.
from .models import Author, Book, Genre, Language, Status, BookInstance

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
admin.site.register(BookInstance)