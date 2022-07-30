from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


CATEGORY = (
    ('Crime', 'Crime'),
    ('Mystery', 'Mystery'),
    ('Rom-Com', 'Rom-Com'),
    ('Sci-fy', 'Sci-fy'),
    ('Action', 'Action'),
    ('Thriller', 'Thriller'),
)


class Book(models.Model):
    bookID = models.CharField(max_length=10, null=True)
    bookName = models.CharField(max_length=50, null=True)
    image = models.ImageField(default='book.jpg', upload_to='books')
    author = models.CharField(max_length=50, null=True)
    publishedDate = models.DateField(null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.bookName}'


def expire():
    return datetime.today() + timedelta(days=14)


class ReserveBook(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reserveDate = models.DateField(auto_now_add=True)
    expireDate = models.DateField(default=expire)

    def __str__(self):
        return f'{self.member}'
