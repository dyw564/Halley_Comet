from django.db import models

class Url(models.Model):
    long_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=100)


    def __unicode__(self):
        return self.long_url



