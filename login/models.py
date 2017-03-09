from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SaveString(models.Model):
    user = models.OneToOneField(User, related_name='saveString')
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.text