from django.db import models

class BreathingData(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    data = models.JSONField()

    def __str__(self):
        return self.id