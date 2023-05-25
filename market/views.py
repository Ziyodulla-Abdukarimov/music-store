from django.shortcuts import render, get_object_or_404
from models.models import Product, Category
from orders.models import OrderItems
from cart.cart import CartSession


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html', {'products': Product.objects.all()[:100]})


def contact(request):
    return render(request, 'contact.html')


def category_detail(request, pk):
    if request.method == 'POST':
        fm = request.POST['from']
        to = request.POST['to']
        if fm and to:
            products = Product.objects.filter(category=pk, price__gt=fm, price__lte=to)
        elif fm:
            products = Product.objects.filter(category=pk, price__gt=fm)
        elif to:
            products = Product.objects.filter(category=pk, price__lte=to)
        else:
            products = Product.objects.filter(category=pk)
    else:
        products = Product.objects.filter(category=pk)
    category_name = Category.objects.get(id=pk).name
    return render(request, 'product.html', {
        'category_name': category_name,
        'products': products
    })


def product_detail(request, pk, id):
    cartSession = CartSession()
    if request.method == 'POST':
        qty = int(request.POST['qty'])
        cartSession.cartAddSession(request, qty, id)

    return render(request, 'product_detail.html', {
        'product': get_object_or_404(Product, id=id),
        'recommended': Product.objects.filter(category=Category.objects.get(id=pk))
    })


def sale_statistics(request):
    product_statistics = OrderItems.objects.all()[:50]
    context = {
        'product_statistics': product_statistics,
    }
    return render(request, 'salestatistics.html', context)


def qty_stat(request):
    context = {
        'qty_stat': Product.objects.all().order_by("-qty")
    }
    return render(request, 'qty_stat.html', context)
