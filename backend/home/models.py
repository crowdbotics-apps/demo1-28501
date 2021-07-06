from django.conf import settings
from django.db import models


class Sample1(models.Model):
    "Generated Model"
    user_id = models.BigIntegerField()
    password = models.TextField()
