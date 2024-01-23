from django.db import models
from authors.models import Author
# Create your models here.

class Book(models.Model):
    # The model representing a book.
    title = models.CharField(max_length=255, blank=False, null=False)
    publish_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=255, null=True)

    def __str__(self):
        # String representation of the Book model.
        return self.title
