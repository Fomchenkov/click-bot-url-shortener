from django.db import models


class UrlСollation(models.Model):
    date = models.DateField()
    token = models.CharField(max_length=20)
    base_url = models.TextField()
    view_count = models.IntegerField(default=0)
