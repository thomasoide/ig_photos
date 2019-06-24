from tastypie.resources import ModelResource
from ig_photos.models import photos

class PhotoResource(ModelResource):
    class Meta:
        queryset = photos.objects.all().order_by('-id')
        resource_name = 'photo'
