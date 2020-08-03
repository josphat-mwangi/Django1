from django.shortcuts import render
from .models import Image

# Create your views here.
def display_images(request):
    photos = Image.photo_display

    return render(request, 'all-photos/photo.html', { "photos": photos})