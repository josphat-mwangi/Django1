from django.db import models

# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    categoryname=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Image(models.Model):
    image_name=models.CharField(max_length=100)
    image_description=models.TextField()
    image_location=models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category=models.ManyToManyField(Category)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.image_name




