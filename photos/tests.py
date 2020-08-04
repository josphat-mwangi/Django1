from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.

class LocationTestClass(TestCase):
    def setUp(self):
        self.nairobi = Location(name='Kenya')
        self.nairobi.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))
    
    
    
    def tearDown(self):
        self.nairobi.delete_location() 

class CategoryTestClass(TestCase):
    def setUp(self):
        self.cupsi = Category(name='Cars')
        self.cupsi.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.cupsi,Category))
    
    def tearDown(self):
        self.cupsi.delete_category()
    

class ImageTestClass(TestCase):
  
   def setUp(self):
        self.jump = Category(name='cars')
        self.jump.save_category()

        self.nairobi = Location(name='Nairobi')
        self.nairobi.save_location()

        self.image = Image(image_name='nature', image_description='have a good one', location=self.nairobi, category=self.jump)
        self.image.save_image()
   def test_instance(self):
       self.assertTrue(isinstance(self.image, Image))

   def test_save_method(self):
       self.image.save_image()
       images = Image.objects.all()
       self.assertTrue(len(images) > 0)

   def test_delete_method(self):
    
       self.image.save_image()
       self.image.delete_image()

   def test_update_method(self):
    
       self.image.save_image()
       new_image = Image.objects.filter(image='image1.jpg').update(photo='download.jpg')
       images = Image.objects.get(image='download.jpg')
       self.assertTrue(images.image, 'download.jpg')

   def test_get_image_by_id(self):
    
       self.image.save_image()
       this_img= self.image.get_image_by_id(self.image.id)
       image = Image.objects.get(id=self.image.id)
       self.assertTrue(this_img, image)

   def test_filter_by_location(self):
      
       self.image.save_image()
       this_img = self.image.filter_by_location(self.image.location_id)
       image = Image.objects.filter(location=self.image.location_id)
       self.assertTrue(this_img, image)

   def test_filter_by_category_name(self):
      
       self.image.save_image()
       images = Image.search_image('this')
       self.assertTrue(len(images)>0)
          
                     