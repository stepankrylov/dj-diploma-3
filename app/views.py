from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from app.models import Phones, Review
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.http import urlencode
from app.forms import UserRegistrationForm, ReviewForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def view_index(request):

    data = Phones.objects.all().order_by('id')[3:]
    template = 'index.html'
    context = {'phones': data}
    return render(request, template, context)


def view_smartphones(request):

    data = Phones.objects.all()
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(data, 3)

    page = paginator.page(page_num)
    new_data = page.object_list

    if page.has_next() == True:
        next_page_url = reverse(view_smartphones) + '?%s' % urlencode({'page': page_num + 1})
    else:
        next_page_url = None

    if page.has_previous() == True:
        prev_page_url = reverse(view_smartphones) + '?%s' % urlencode({'page': page_num - 1})
    else:
        prev_page_url = None

    template = 'smartphones.html'

    context = {'phones': new_data,
               'current_page': page,
               'prev_page_url': prev_page_url,
               'next_page_url': next_page_url,
               }
    return render(request, template, context)


def view_phone(request, slug):

    template = 'phone.html'
    form = ReviewForm(request.POST)
    a = request.POST.get("name")
    b = request.POST.get("content")

    phone = Phones.objects.get(slug=slug)
    context = {'phone': phone,
               'form': form}
    return render(request, template, context)


def view_empty_section(request):

    template = 'empty_section.html'
    context = {}
    return render(request, template, context)


def view_cart(request):

    template = 'cart.html'

    context = {}
    return render(request, template, context)


def view_login(request):
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data

        username = data['username']
        email = data['email']
        password = data['password']

        user = authenticate(username=username, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
        else:
            new_user = form.save(commit=False)
            new_user.email = email
            new_user.set_password(password)
            new_user.save()
            login(request, new_user)


    template = 'login.html'
    context = {'user_form': form}
    return render(request, template, context)


def view_logout(request):
    logout(request)

    template = 'login.html'
    context = {}
    return render(request, template, context)
