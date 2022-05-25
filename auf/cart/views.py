from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from board.models import Books
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, book_id):
    print('1')
    cart = Cart(request)
    print(book_id, '1233')
    book = get_object_or_404(Books, id=book_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print(cd, '123')
        cart.add(book=book,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    print('2')
    book = get_object_or_404(Books, id=product_id)
    cart.remove(book)
    return redirect('detail2.html')

def cart_detail(request):
    print('3')
    cart = Cart(request)
    print(request)
    return render(request, 'detail2.html', {'cart': cart})
