from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    cover_image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(5.00)])

    def __str__(self):
        return self.name