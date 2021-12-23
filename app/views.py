"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import PoolForm
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Blog
from .models import Pizza
from .models import Sup
from .models import Roll
from .models import Comment
from .models import CommentZ
from .forms import CommentForm
from .forms import CommentZForm
from .forms import BlogForm
from django.utils.decorators import method_decorator

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами.',
            'year':datetime.now().year,
        }
    )

def MZakaz(request):
    """Renders the MZakaz page."""
    commentsz = CommentZ.objects.filter(author=request.user)
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        form = CommentZForm(request.POST)
        if form.is_valid():
            commentz_f = form.save(commit=False)
            commentz_f.author = request.user
            commentz_f.date = datetime.now()
            commentz_f.save()
            return redirect('contact')
    else:
        form = CommentZForm()

    return render(
        request,
        'app/MZakaz.html',
        {
            'title':'Мои заказы',
            'message':'Страница с историей ваших заказов.',
            'commentsz': commentsz,
            'form': form,
            'year':datetime.now().year,
        }
    )

def zakaz(request):
    """Renders the MZakaz page."""
    commentsz = CommentZ.objects.filter()
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        form = CommentZForm(request.POST)
        if form.is_valid():
            commentz_f = form.save(commit=False)
            commentz_f.author = request.user
            commentz_f.date = datetime.now()
            commentz_f.save()
            return redirect('contact')
    else:
        form = CommentZForm()

    return render(
        request,
        'app/zakaz.html',
        {
            'title':'Заказы',
            'message':'Страница с заказами клиентов.',
            'commentsz': commentsz,
            'form': form,
            'year':datetime.now().year,
        }
    )

def catalog(request):
    """Renders the catalog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/catalog.html',
        {
            'title':'Каталог',
            'message':'Выберите подходящий раздел с нашими продуктами',
            'year':datetime.now().year,
        }
    )

def blog(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all()
    return render(
        request,
        'app/blog.html',
        {
            'title':'Блог',
            'posts': posts,
            'year':datetime.now().year,
        }
    )

def pizza(request):
    """Renders the pizza page."""
    assert isinstance(request, HttpRequest)
    posts = Pizza.objects.all()
    return render(
        request,
        'app/pizza.html',
        {
            'title':'Пицца',
            'posts': posts,
            'year':datetime.now().year,
        }
    )

def sup(request):
    """Renders the sup page."""
    assert isinstance(request, HttpRequest)
    posts = Sup.objects.all()
    return render(
        request,
        'app/sup.html',
        {
            'title':'Супы',
            'posts': posts,
            'year':datetime.now().year,
        }
    )

def roll(request):
    """Renders the roll page."""
    assert isinstance(request, HttpRequest)
    posts = Roll.objects.all()
    return render(
        request,
        'app/roll.html',
        {
            'title':'Роллы',
            'posts': posts,
            'year':datetime.now().year,
        }
    )

def blogpost(request, parametr):
    """Renders the blogpost page."""
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()
            return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1,
            'comments': comments,
            'form': form,
            'year':datetime.now().year,
        }
    )

def pizzapost(request, parametr2):
    """Renders the pizzapost page."""
    post_2 = Pizza.objects.get(id=parametr2)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/pizzapost.html',
        {
            'post_2': post_2,
            'year':datetime.now().year,
        }
    )

def suppost(request, parametr3):
    """Renders the suppost page."""
    post_3 = Sup.objects.get(id=parametr3)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/suppost.html',
        {
            'post_3': post_3,
            'year':datetime.now().year,
        }
    )

def rollpost(request, parametr4):
    """Renders the rollpost page."""
    post_4 = Roll.objects.get(id=parametr4)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/rollpost.html',
        {
            'post_4': post_4,
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'АППЕТИТНЫЕ СУШИ И РОЛЛЫ С ДОСТАВКОЙ НА ДОМ',
            'year':datetime.now().year,
        }
    )

def links(request):
    """Renders the links page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Полезные сведения',
            'message':'Перейди по ссылкам-иконкам на похожие полезные интернет-ресурсы!',
            'year':datetime.now().year,
        }
    )

def pool(request):
    assert isinstance(request, HttpRequest)
    data = None
    design = {'1': 'Отлично', '2': 'Хорошо', '3': 'Нормально', '4': 'Плохо', '5': 'Очень плохо',}
    functio = {'1': 'Отлично', '2': 'Хорошо', '3': 'Нормально', '4': 'Плохо', '5': 'Очень плохо',}
    internet = {'1': 'Каждый день', '2': 'Несколько раз в день', '3': 'Несколько раз в неделю', '4': 'Несколько раз в месяц'}
    if request.method == 'POST':
        form = PoolForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['design'] = design[ form.cleaned_data['design']]
            data['functio'] = functio[ form.cleaned_data['functio']]
            data['internet'] = internet[ form.cleaned_data['internet']]
            if(form.cleaned_data['notice'] == True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['message'] = form.cleaned_data['message']
            form = None
    else:
        form = PoolForm()
    return render(
        request,
        'app/pool.html',
        {
            'form':form,
            'data':data
        }
    )

def registration(request):
    """Renders the registration page."""

    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()

            regform.save()

            return redirect('home')
    else:
        regform = UserCreationForm()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
                
            'regform': regform,
                
            'year':datetime.now().year,
        }
    )

def newpost(request):
    """Renders the newpost page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()

            return redirect('blog')
    else:
        blogform =  BlogForm()


    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,
            'title': 'Добавить статью блога',
            
            'year':datetime.now().year,
        }
    )

def newzakaz(request):
    """Renders the newzakaz page."""
    commentsz = CommentZ.objects.filter(author=request.user)
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        form = CommentZForm(request.POST)
        if form.is_valid():
            commentz_f = form.save(commit=False)
            commentz_f.author = request.user
            commentz_f.date = datetime.now()
            commentz_f.save()
            return redirect('contact')
    else:
        form = CommentZForm()

    return render(
        request,
        'app/newzakaz.html',
        {
            'title': 'Добавить заказ',
            'commentsz': commentsz,
            'form': form,
            'year':datetime.now().year,
        }
    )

def videopost(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видеоресурс',
            'year':datetime.now().year,
        }
    )