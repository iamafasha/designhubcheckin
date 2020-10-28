from django.db import models
from django.utils import timezone

# Create your models here.
class Visitors(models.Model):
    name = models.CharField(max_length=200)
    identification_number = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=200)
    telephone_number = models.IntegerField()
      

    def __str__(self):
        return self.name


class Checkins(models.Model):
    visitor = models.ForeignKey(Visitors, on_delete=models.CASCADE)
    #use floatfield
    temperature = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    def checkin(self):
        self.save()

    def __str__(self):
        return str(self.visitor)