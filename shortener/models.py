from django.db import models


class UrlСollation(models.Model):
    token = models.CharField(max_length=20)
    base_url = models.TextField(default=0)
