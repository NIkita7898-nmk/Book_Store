from django.db import models
from books.models import Book
from django.core.validators import MinValueValidator

# Create your models here.

class Information(models.Model):
    # Additional information related to a book, like quantity.
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity= models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField()

    def __str__(self):
        # String representation of the Information model.
        return f"{self.book.title} - Quantity: {self.quantity}"
