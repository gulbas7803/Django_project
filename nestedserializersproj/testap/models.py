from django.db import models


class Author(models.Model):
    objects = True
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)

    def __str__(self):
        return self.first_name


class Book(models.Model):
    objects = True
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_by_author')
    release_date = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title
