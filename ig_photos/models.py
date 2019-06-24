from django.db import models

class photos(models.Model):

    # Unique identifier for each photo in the DATABASE
    id = models.AutoField(
        primary_key=True,
    )

    url = models.CharField(
        max_length=200,
    )

    photo = models.ImageField(

    )
    photo_slug = models.CharField(
        max_length=100,
    )

    alt_text = models.CharField(
        max_length=100,
        default="Instagram Photo",
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True,
    )
