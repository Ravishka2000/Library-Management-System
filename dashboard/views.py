from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, ReserveBook
from .forms import BookForm


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
        form = BookForm(request.POST,request.FILES, instance=book)
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
    categories = Book.objects.values_list('category', flat=True).distinct()
    context = {
        "books": books,
        "categories": categories,
    }
    if request.method == 'POST':
        if 'Thriller' in request.POST:
            queryset = books.filter(category='Thriller')
            categories = queryset.values_list('category', flat=True).distinct()
            context = {
                "books": queryset,
                "categories": categories,
                "reset": "Reset",
            }
        elif 'Sci-fy' in request.POST:
            queryset = books.filter(category='Sci-fy')
            categories = queryset.values_list('category', flat=True).distinct()
            context = {
                "books": queryset,
                "categories": categories,
                "reset": "Reset",
            }
        elif 'Crime' in request.POST:
            queryset = books.filter(category='Crime')
            categories = queryset.values_list('category', flat=True).distinct()
            context = {
                "books": queryset,
                "categories": categories,
                "reset": "Reset",
            }
        elif 'Mystery' in request.POST:
            queryset = books.filter(category='Mystery')
            categories = queryset.values_list('category', flat=True).distinct()
            context = {
                "books": queryset,
                "categories": categories,
                "reset": "Reset",
            }
        elif 'Rom-Com' in request.POST:
            queryset = books.filter(category='Rom-Com')
            categories = queryset.values_list('category', flat=True).distinct()
            context = {
                "books": queryset,
                "categories": categories,
                "reset": "Reset",
            }
        elif 'Action' in request.POST:
            queryset = books.filter(category='Action')
            categories = queryset.values_list('category', flat=True).distinct()
            context = {
                "books": queryset,
                "categories": categories,
                "reset": "Reset",
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
        book = Book.objects.get(id=pk)
        reserve = ReserveBook.objects.create(member=current_user, book=book)
        reserve.save()
    return redirect('book-reserve')


