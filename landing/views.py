from django.shortcuts import render
from rest_framework.decorators import api_view

from .forms import SubscriberForm
from products.models import *
from django.contrib import auth
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout


#
# def login(request):
#     username = request.POST['name']
#     password = request.POST['password']
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         # Правильный пароль и пользователь "активен"
#         auth.login(request, user)
#         # Перенаправление на "правильную" страницу
#         return HttpResponseRedirect("landing/home.html")
#     else:
#         # Отображение страницы с ошибкой
#         return HttpResponseRedirect("landing/landing.html")
# def landing(request):
#     name = "CodingMedved"
#     current_day = "03.01.2017"
#
#     items = []
#     items.append("product.name")


# FAKE METHOD::
# b = items.amount()
# form = SubscriberForm(request.POST or None)
#
# if request.method == "POST" and form.is_valid():
#     print(request.POST)
#     print(form.cleaned_data)
#     data = form.cleaned_data
#     print(data["name"])
#
#     new_form = form.save()
#
# return render(request, 'landing/landing.html')


#
#
#
class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "login"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "home"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")


@api_view(['GET'])
def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_ring = products_images.filter(product__category__id=2)
    products_images_bracelet = products_images.filter(product__category__id=1)
    products_images_pendant = products_images.filter(product__category__id=3)
    # return render(request, 'landing/home.html', {'products_images':products_images})
    return render(request, 'landing/home.html',
                  {"products_images": products_images, "products_images_ring": products_images_ring,
                   "products_images_bracelet": products_images_bracelet,"products_images_pendant":products_images_pendant })
