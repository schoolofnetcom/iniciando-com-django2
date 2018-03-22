from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category


# Create your views here.
# MVC - Model View Controller

# M - models.py
# V - html
# C - views.py

# MTV
# M - models.py
# T - template
# V - views.py

# Twig - Django Template
# Jinja - Django Templates

def home(request):
    return HttpResponse('Olá mundo!!')


def home_param(request, post_id):
    return HttpResponse('Olá mundo!! %s' % post_id)


def post_list(request):
    # name = 'Luiz Carlos'
    # return render(request, 'post_list.html', {'name': name})
    if 'category_id' in request.GET:
        #category = Category.objects.get(id=request.GET['category_id'])
        #posts = Post.objects.filter(categories=category)
        posts = Post.objects.filter(categories=request.GET['category_id'])
    else:
        posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'post_list.html', {
        'posts': posts,
        'categories': categories
    })


def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.all()
    return render(request, 'post_show.html', {
        'post': post,
        'categories': categories
    })