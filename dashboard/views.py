from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def index(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'dashboard/index.html', context)


def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
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


def deletebook(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(id=pk)
        book.delete()
        return redirect('dashboard-index')
    return render(request, 'dashboard/bookdelete.html')
