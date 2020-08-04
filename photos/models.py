from django.db import models

# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
class Image(models.Model):
    image_name=models.CharField(max_length=100)
    image_description=models.TextField()
    location=models.ForeignKey('Location',on_delete=models.CASCADE)
    category=models.ManyToManyField(category)
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

    def __str__(self):
        return self.image_name




