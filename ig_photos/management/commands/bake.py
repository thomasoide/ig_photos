import os, requests, json, boto3
import botocore
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DataError
from ig_photos.models import photos
from django.core.management import call_command
from ig_photos.models import photos

class Command(BaseCommand):
    """
    Bakes out database output as json
    """
    def handle(self, *args, **kwargs):
        bucketName = "static.startribune.com"

        outputName = "assets/features/thomas/ig_photos.json"

        Key1 = "assets/features/thomas/ig_photos.json"
        output1 = "assets/features/thomas/old_ig_photos.json"

        filename = "ig_photos.json"
        old_filename = "old_ig_photos.json"
        # url = "http://localhost:8000/api/ig_photos/photo/?format=json"
        url = "http://ec2-13-57-84-236.us-west-1.compute.amazonaws.com/ig-photos/api/ig_photos/photo/?format=json"

        s3 = boto3.resource('s3')
        try:
            s3.Bucket(bucketName).download_file(Key1, output1)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

        self.stdout.write('Baking database to JSON...', ending="\n")
        resp = requests.get(url=url,)
        json_data = json.loads(resp.text)

        with open('%s' % filename, 'w') as outfile:
            json.dump(json_data, outfile)

        s3 = boto3.client('s3')
        s3.upload_file(filename, bucketName, outputName)
        s3.upload_file(old_filename, bucketName, output1)
