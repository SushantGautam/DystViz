from django.db import models


# Create your models here.
class VideoAnnotations(models.Model):
    type = models.CharField(max_length=100)
    pid = models.IntegerField()
    start = models.IntegerField( null=True, blank=True)
    end = models.IntegerField( null=True, blank=True)

    class Meta:
        unique_together = ('type', 'pid',)
