from django.db import models


CATEGORY = (
    ('Crime', 'Crime'),
    ('Mystery', 'Mystery'),
    ('Rom-Com', 'Rom-Com'),
    ('Sci-fy', 'Sci-fy'),
)


class Book(models.Model):
    bookID = models.CharField(max_length=10, null=True)
    bookName = models.CharField(max_length=50, null=True)
    author = models.CharField(max_length=50, null=True)
    publishedDate = models.DateField(null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.bookName} {self.category}'
