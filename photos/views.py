from django.shortcuts import render
from .models import Image

# Create your views here.
def display_images(request):
    photos = Image.photo_display

    return render(request, 'all-photos/photo.html', { "photos": photos})
def search_results(request):
    '''
    search function to display search search_results
    args:
    order defines category
    '''
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html', {"message": message})
def image(request,image_id):
    try:
        image = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/item.html",{"image":image})