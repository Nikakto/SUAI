from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse


from SUAI import const, staff
from SUAI.staff.forms import *


import re


def about(request):
    return render(request, 'about.html')


def gallery(request):
    
    images_list = Image.objects.filter(removed=0)

    if request.user.is_authenticated:
        paginator = Paginator(images_list, 15)
    else:
        paginator = Paginator(images_list, 16)
    
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)

    return render(request, 'gallery.html', {'images': images})


def gallery_upload(request):

    if not request.user.is_authenticated:
        return redirect(reverse('gallery'))

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('gallery'))

    else:
        form = ImageForm()

        source = form.fields['source']
        source.label = ''
        source.widget.attrs['onchange'] = 'getName(this.value);'
        source.widget.attrs['accept'] = "image/jpeg,image/png,image/gif"

        name = form.fields['name']
        name.label = ''
        name_widget = form.fields['name'].widget
        name_widget.attrs['class'] = 'gallery-upload-input-string'
        name_widget.attrs['placeholder'] = 'Title'

        description = form.fields['description']
        description.label = ''
        description_widget = form.fields['description'].widget
        description_widget.attrs['class'] = 'gallery-upload-input-textarea'
        description_widget.attrs['placeholder'] = 'Description'
        description_widget.attrs['rows'] = '7'

    return render(request, 'base.html', {'form': form})


def calculator(request):
    return render(request, 'converter.html', {'units': const.LIST_OF_UNITS})


def index(request):
    return render(request, 'index.html')


def news(request):

    if request.method == 'POST':

        form = NewsForm(request.POST)
        if form.is_valid():

            content = form.cleaned_data['content']
            title = form.cleaned_data['title']
            user = request.user

            news = News(content=content, title=title, user=user)
            news.save()

            redirect(reverse('index'))

    return redirect(reverse('index'))


def user_logining(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        referer = request.META['HTTP_REFERER']
        if not referer:
            referer = reverse('index')

        if user is not None:
            login(request, user)

        return HttpResponseRedirect(referer)

    elif request.method == 'GET':
        return redirect(reverse('index'))


def user_logout(request):

    if request.method == 'POST':
        logout(request)
        return redirect(reverse('index'))

    return redirect(reverse('index'))


def user_register(request):

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    form = UserRegisterForm()

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if not form.data['username']:
            form.errors['username'] = 'Please, entry your login'
        elif len(form.data['username']) < 3:
            form.errors['username'] = 'Login is too short'
        elif User.objects.filter(username=form.data['username']):
            form.errors['username'] = 'The name is use'
        else:
            username_matches = re.fullmatch('[a-z0-9.]*', form.data['username'])
            if not username_matches or username_matches.group(0) != form.data['username']:
                form.errors['username'] = 'Login contains unexpected symbols'

        if not form.data['password']:
            form.errors['password'] = 'Please, entry password'
            form.errors['password_again'] = form.errors['password']
        elif len(form.data['password']) < 6:
            form.errors['password'] = 'Password is too short'
        elif form.data['password'] != form.data['password_again']:
            form.errors['password'] = 'Passwords aren\'t match'
            form.errors['password_again'] = form.errors['password']
        else:
            if not staff.is_ascii(form.data['password']):
                form.errors['password'] = 'Password contains unexpected symbols'

        mail_matches = re.fullmatch('[a-z0-9.]{1,50}@[a-z0-9]{1,10}.[a-z]{1,10}', form.data['email'])
        if not mail_matches:
            form.errors['email'] = 'Please, entry correct email'
        elif User.objects.filter(email=form.data['email']):
            form.errors['email'] = 'The email is use'

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            User.objects.create_user(username, email, password)

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

            return redirect(reverse('index'))

    return render(request, 'base.html', {'form': form})
