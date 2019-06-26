import os
import requests
import json
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DataError
from ig_photos.models import photos
from django.core.management import call_command
from ig_photos.api import PhotoResource
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from ig_photos.models import photos

class Command(BaseCommand):
    """
    Bakes out database output as json
    """
    def handle(self, *args, **kwargs):
        filename = "ig_photos.json"
        url = "http://localhost:8000/api/ig_photos/photo/?format=json"
        # save_path =
        self.stdout.write('Baking database to JSON...', ending="\n")
        resp = requests.get(url=url,)
        json_data = json.loads(resp.text)

        with open('%s' % filename, 'w') as outfile:
            json.dump(json_data, outfile)
