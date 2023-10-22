from django.http import HttpResponse
from django.shortcuts import render

from marshallite_cart.context_processor import cart_total_amount
from .tasks import order_created
from mainsite.models import Product
from .models import OrderItem, Order
from .forms import OrderCreateForm
from marshallite_cart.cart import Cart


def order_create(request):
    if not request.user.id:
        return HttpResponse('Unauthorized', status=401)

    cart = Cart(request)
    print(request.user.id)

    if request.method == 'POST':
        order = Order.objects.create(
            user_id=request.user.id,
            order_sum=cart_total_amount(request).get('cart_total_bill')
        )

        for item in cart:
            print(item)
            print(order)
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        order_created.delay(order.id)
        return render(request, 'order/created.html', {'order': order})
    else:
        return render(request, 'order/create.html', {'cart': cart})
