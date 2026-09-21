from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from main.models import Advertisement
from .models import Order, OrderProduct


@login_required(login_url='login')
def to_cart(request, ad_id: int, action: str):
    """action: add - 1 taga qo'shish, delete - 1 taga kamaytirish, remove - butunlay olib tashlash"""
    product = get_object_or_404(Advertisement, pk=ad_id)
    order, created = Order.objects.get_or_create(user=request.user, status="tan")

    if action == "add":
        order_product, created = OrderProduct.objects.get_or_create(order=order, product=product)
        order_product.quantity += 1
        order_product.save()
    elif action == "delete":
        order_product = OrderProduct.objects.filter(order=order, product=product).first()
        if order_product:
            order_product.quantity -= 1
            if order_product.quantity <= 0:
                order_product.delete()
            else:
                order_product.save()
    elif action == "remove":
        OrderProduct.objects.filter(order=order, product=product).delete()

    return redirect('cart')


@login_required(login_url='login')
def cart(request):
    order = Order.objects.filter(user=request.user, status="tan").first()
    items = order.items.select_related("product") if order else []
    context = {
        'order': order,
        'items': items,
        'total': order.get_total() if order else 0,
    }
    return render(request, 'order/cart.html', context)


@login_required(login_url='login')
def checkout(request):
    order = Order.objects.filter(user=request.user, status="tan").first()
    if not order or not order.items.exists():
        return redirect('cart')

    if request.method == 'POST':
        order.address = request.POST['address']
        order.price = order.get_total()
        order.status = "jar"
        order.save()
        return redirect('orders')

    context = {
        'order': order,
        'items': order.items.select_related("product"),
        'total': order.get_total(),
    }
    return render(request, 'order/checkout.html', context)


@login_required(login_url='login')
def orders(request):
    orders = Order.objects.filter(user=request.user).exclude(status="tan").order_by('-created')
    return render(request, 'order/orders.html', {'orders': orders})


@login_required(login_url='login')
def cancel_order(request, order_id: int):
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    if order.status == "jar" and request.method == 'POST':
        order.status = "bekor"
        order.save()
    return redirect('orders')
