from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from mainsite.models import Product
from mainsite.utils import footer_fourth_col, footer_third_col, footer_second_col, footer_first_col
from orders.views import order_create
from .cart import Cart


@login_required(login_url="/login")
def cart_add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="/users/login")
def item_increment(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="/users/login")
def item_decrement(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.decrement(product=product)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login')
def item_clear(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER'))


def cart_detail(request):
    cart = Cart(request)
    if request.method == 'POST':
        order_create(request)

    return render(request, 'marshallite_cart/detail.html', {
        'cart': cart,
        'footer_first_col': footer_first_col,
        'footer_second_col': footer_second_col,
        'footer_third_col': footer_third_col,
        'footer_fourth_col': footer_fourth_col
    })
