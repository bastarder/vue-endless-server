from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SaveString(models.Model):
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.text