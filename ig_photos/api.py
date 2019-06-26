from tastypie.resources import ModelResource
from ig_photos.models import photos
from tastypie.serializers import Serializer

class PhotoResource(ModelResource):
    class Meta:
        queryset = photos.objects.all().order_by('-id')
        resource_name = 'photo'
        limit = 50
        serializer = Serializer(formats=['json'])
