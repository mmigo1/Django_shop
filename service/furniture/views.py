from django.shortcuts import render, get_object_or_404, redirect

from .models import Furniture

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .forms import FurnitureForm, ContactForm, LoginForm, RegistrationForm
# Пагинатор
from django.core.paginator import Paginator
# Почта
from django.core.mail import send_mail
from django.conf import settings
# Логин и регистрация
from django.contrib.auth import login, logout

# Декораторы
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
# Корзина
from basket.forms import BasketAddProductForm
# API

from .serializer import FurnitureSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def index(request):
    return render(request=request, template_name='furniture/index.html')


class FurnitureListView(ListView):
    model = Furniture
    template_name = 'furniture/furniture-list.html'

    context_object_name = 'furniture'
    paginate_by = 2


class FurnitureDetailView(DetailView):
    model = Furniture
    template_name = 'furniture/furniture-info.html'
    context_object_name = 'one_furniture'
    pk_url_kwarg = 'furniture_id'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FurnitureDetailView, self).get_context_data(**kwargs)
        basket = BasketAddProductForm()
        context['basket_form'] = basket
        return context


class FurnitureCreateView(CreateView):
    model = Furniture
    form_class = FurnitureForm
    template_name = 'furniture/furniture-add.html'

    context_object_name = 'form'
    success_url = reverse_lazy('furn_list')

    @method_decorator(permission_required('furniture.add_furniture'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class FurnitureUpdateView(UpdateView):
    model = Furniture
    form_class = FurnitureForm
    template_name = 'furniture/furniture-edit.html'
    context_object_name = 'form'

    @method_decorator(permission_required('furniture.change_furniture'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class FurnitureDeleteView(DeleteView):
    model = Furniture
    success_url = reverse_lazy('furn_list')

    @method_decorator(permission_required('furniture.delete_furniture'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def contact_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['content'],
                settings.EMAIL_HOST_USER,
                ['mmigo1@mail.ru'],
                fail_silently=True
            )
            if mail:
                return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'furniture/email.html', {'form': form})


def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'furniture/auth/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'furniture/auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('log in')


@api_view(['GET', 'POST'])
def furniture_api_list(request):
    if request.method == 'GET':
        furniture_list = Furniture.objects.all()
        serializer = FurnitureSerializer(furniture_list, many=True)
        return Response({'furn_list': serializer.data})
    elif request.method == 'POST':
        serializer = FurnitureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def furniture_api_detail(request, pk, format=None):
    furn_obj = get_object_or_404(Furniture, pk=pk)
    if furn_obj.exist:
        if request.method == 'GET':
            serializer = FurnitureSerializer(furn_obj)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = FurnitureSerializer(furn_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Данные успешно обновлены', 'furn': serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            furn_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
