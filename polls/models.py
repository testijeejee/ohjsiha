from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Note(models.Model):
    pub_date = models.DateTimeField('muistiinpanon päiväys')
    notetitle = models.CharField(max_length=50)
    notes = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.notetitle

    class Meta:
        ordering=['-pub_date']
