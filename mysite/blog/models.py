from __future__ import unicode_literals
from django.db import models
from froala_editor.fields import FroalaField

class Post(models.Model):
  title = models.CharField(max_length=140)
  body = FroalaField()
  date = models.DateTimeField()

  def __unicode__(self):
    return self.title
