from django.db import models

class class_contents(models.Model):
    keyword = models.CharField(max_length=200)
    content = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()