from django.shortcuts import render
from .models import BlogPost, Contact, MainPost

def index(request):
    posts = MainPost.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'main/index.html', context)

def contacts(request):
    contacts = Contact.objects.all()

    context = {
        'contacts': contacts,
    }

    return render(request, 'main/contacts.html', context)

def blog(request):
    posts = BlogPost.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'main/blog.html', context)
