from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def products_list(request):
    products = Product.objects.all().order_by('name')
    return render(request,
                  'products/list.html',
                  {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id)
    return render(request,
                  'products/detail.html',
                  {'product': product})