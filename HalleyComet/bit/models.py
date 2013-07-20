from django.db import models
from django.contrib.auth.models import User
class Url(models.Model):
    long_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=30)
    visit_time = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return self.long_url
