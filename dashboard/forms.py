from django import forms
from .models import *
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['bookID', 'bookName', 'author', 'category', 'publishedDate', 'quantity', 'image']


class BookBorrow(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['bookName', 'author', 'category']
