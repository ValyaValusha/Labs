from .models import ProductInBasket
from django.http import Http404, HttpResponse


def getting_basket_info(request):
    # session_key = request.session.session_key
    # if not session_key:
    #     request.session.cycle_key()

    products_in_basket = ProductInBasket.objects.filter(user=request.user, is_active=True) if request.user.is_authenticated else []
    products_total_nmb = products_in_basket.count() if request.user.is_authenticated else 0

    return locals()