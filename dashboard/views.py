from django.shortcuts import render, redirect
from .models import Book


def index(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'dashboard/index.html', context)
