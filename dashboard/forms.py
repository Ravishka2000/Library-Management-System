from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['bookID', 'bookName', 'author', 'category', 'publishedDate', 'quantity', 'image']

