from django.db import models

# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
class Image(models.Model):
    image_name=models.CharField(max_length=100)
    image_description=models.TextField()
    location=models.ForeignKey('Location',on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)
    image = models.ImageField(upload_to = 'images/', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def photo_display(cls):
       photos = cls.objects.filter()
       return photos 

    @classmethod
    def search_by_category(cls, search_term):
        display = cls.objects.filter(category__name__icontains=search_term)
        return display
    @classmethod
    def filter_by_location(cls):
        display = cls.objects.filter(
            location__name__icontains='Silicon Valley')
        return display

    def __str__(self):
        return self.image_name




