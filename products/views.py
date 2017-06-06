from django.shortcuts import render
from products.models import *


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/product.html', locals())


    if not request.user.is_authenticated:
        return HttpResponse(401)


    return render(request, 'products/product.html', locals())