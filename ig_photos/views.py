from django.shortcuts import render
from django.http import HttpResponse
from ig_photos.models import photos
import requests

def index(request):
    photo_list = photos.objects.all().order_by('-id')
    context = { 'photo_list': photo_list }
    return render(request, 'ig_photos/index.html', context)
