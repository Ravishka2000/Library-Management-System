from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Book, ReserveBook
from .forms import BookForm, BookBorrow


@login_required
def index(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'dashboard/index.html', context)


@login_required
def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = BookForm()
    context = {
        "heading": "Add Book",
        "form": form,
        "button": "Add",
    }
    return render(request, 'dashboard/addbook.html', context)


@login_required
def updatebook(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = BookForm(instance=book)
    context = {
        "heading": "Update Book",
        "form": form,
        "button": "Update",
    }
    return render(request, 'dashboard/addbook.html', context)


@login_required
def deletebook(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(id=pk)
        book.delete()
        return redirect('dashboard-index')
    return render(request, 'dashboard/bookdelete.html')


@login_required
def viewbooks(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'dashboard/allbooks.html', context)


@login_required
def reservebooks(request):
    books = ReserveBook.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'dashboard/reservebooks.html', context)


@login_required
def borrowbook(request, pk):
    if request.method == 'POST':
        current_user = request.user
        membername = current_user.username
        book = Book.objects.get(id=pk)
        reserve = ReserveBook.objects.create(member=membername, bookID=book.bookID)
        reserve.save()
    return redirect('book-view')


