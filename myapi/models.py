from django.db import models
# Create your models here.


class WeatherInfo(models.Model):
    temperature = models.FloatField()
    date_recorded  = models.DateField()

    def __str__(self):
        return "{\"temperature\":"+str(self.temperature)+",\"date_recorded\":\""+str(self.date_recorded)+"\"}"
