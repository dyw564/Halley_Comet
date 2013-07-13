from django.db import models

# Create your models here.


class url(models.Model):
    long_url = CharField(max_length=200)
    short_url = CharField(max_length=100)

    def __unicode__()

