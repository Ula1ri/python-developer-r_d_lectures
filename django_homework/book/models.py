from django.db import models


# Create your models here.

class Book(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField(null=False)
    prise = models.PositiveIntegerField(null=False)

    class Meta:
        db_table = 'book'
