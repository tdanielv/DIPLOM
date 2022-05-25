
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import title
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST
from django.views.generic import CreateView
from cart.forms import CartAddProductForm

from .forms import AddItemForm, AddAuthorForm, AddYearForm, AddGenreForm, SearchForm
from .models import Books, Author, Year, Genre, BookInstance



def index(request):
    books = Books.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'books': books, 'num_visits': num_visits}
    return render(request, 'main_page.html', context)

# def add_new(request):
#     if request.method == "POST":
#         form = AddItemForm(request.POST)
#         if form.is_valid():
#             book = form.cleaned_data
#             print(book)
#             book.save()
#     return render(request, 'main_page.html')

class AddBookView(CreateView):
    template_name = 'add_new.html'
    form_class = AddItemForm
    success_url = reverse_lazy('main_page')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['addnew'] = ['genre', 'year', 'author']
    #     print(context)
    #     return context

def year_add(request):
    year = Year.objects.all()
    form = AddYearForm(request.POST)
    if request.method == 'POST':
        form = AddYearForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['year']
            try:
                year = Year.objects.get(year__iexact=a)
                print('Введите заново')
                context = {'form': form}
                return render(request, 'add_year.html', context)
            except:
                form.save()
                return redirect('add')
    context = {'form': form}
    return render(request, 'add_year.html', context)

def author_add(request):
    author = Author.objects.all()
    form = AddAuthorForm(request.POST)
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['author']
            try:
                author = Author.objects.get(author__iexact=a)
                # if author:
                #     ValidationError('')
                # else:
                #     form.save()
                print('Введите заново')
                context = {'form': form}
                return render(request, 'add_author.html', context)
            except:
                form.save()
                return redirect('add')
    context = {'form': form}
    return render(request, 'add_author.html', context)

def genre_add(request):
    genre = Genre.objects.all()
    form = AddGenreForm(request.POST)
    if request.method == 'POST':
        form = AddGenreForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['genre']
            try:
                genre = Genre.objects.get(genre__iexact=a)
                print('Введите заново')
                context = {'form': form}
                return render(request, 'add_genre.html', context)
            except:
                form.save()
                return redirect('add')
    context = {'form': form}
    return render(request, 'add_genre.html', context)
# class AddAuthorView(CreateView):
#     template_name = 'add_author.html'
#     form_class = AddAuthorForm
#     success_url = reverse_lazy('add')
#
#     def get(self, request):
#         author = Author.objects.all()
#         print(author)
#         errors = {}
#         # if self.cleaned_data['author'] in author:
#         #     errors['author'] = ValidationError('Данный автор уже имеется')
def detail(request, book_id):
    print( request.POST,'4')
    book = get_object_or_404(Books, id = book_id)
    cart_product_form = CartAddProductForm(request.POST)
    # print(book,'12', book_id)
    return render(request, 'detail.html', {'book': book, 'cart_product_form': cart_product_form})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id = author_id)
    books = Books.objects.filter(author_id=author_id)
    return render(request, 'author_detail.html', {'author': author, 'books': books})

def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, id = genre_id)
    books = Books.objects.filter(genre_id=genre_id)
    return render(request, 'genre_detail.html', {'genre': genre, 'books': books})

def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})

def genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres.html', {'genres': genres})

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

def search(request):
    books = Books.objects.all()
    form = SearchForm()
    l = {}
    if request.method=='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            f = f['title']
            for i in books:
                if f in i.title :
                    l[i] = i

    context = {'form': form, 'list': l}
    return render(request, 'search.html', context)
