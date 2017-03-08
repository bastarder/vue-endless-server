from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SaveString(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.text