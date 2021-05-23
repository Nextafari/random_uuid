from django.db import models

class RandomId(models.Model):
    class Meta:
        verbose_name = "Random ID"
        verbose_name_plural = "Random IDs"
    random_uuid = models.CharField(max_length=150)
    time_created = models.CharField(max_length=150)
