from django.contrib import admin

# Register your models here.
from .models import Author, Book, Genre, Language, Status, BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'data_of_birth', 'data_of_death')
    fields = ['first_name', 'last_name', ('data_of_birth', 'data_of_death')]


admin.site.register(Author, AuthorAdmin)

# admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
# admin.site.register(BookInstance)



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
