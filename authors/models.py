from django.db import models

# Create your models here.

class Author(models.Model):
    # The model representing an author.
    name = models.CharField(max_length=255, null=False, blank=False)
    birth_date = models.DateField()

    def __str__(self):
        # String representation of the Author model.
        return self.name
