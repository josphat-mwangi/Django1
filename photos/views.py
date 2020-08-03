from django.shortcuts import render
from .models import Image

# Create your views here.
def display_images(request):
    photos = Image.photo_display

    return render(request, 'all-photos/photo.html', { "photos": photos})
def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        search_images = Image.search_by_title(category)
        message = f"{category}"

        return render(request, 'all-photos/search.html',{"message":message,"images":search_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/item.html",{"image":image})