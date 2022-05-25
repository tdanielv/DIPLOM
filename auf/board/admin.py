from django.contrib import admin

from .models import Books, Author, Genre, Year, BookInstance

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status','borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back','borrower')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ( 'Доступность', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'year']
    search_fields = ['__all__']
    inlines = [BookInstanceInline]

admin.site.register(Books, BooksAdmin)
admin.site.register(Year)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(BookInstance, BookInstanceAdmin)
