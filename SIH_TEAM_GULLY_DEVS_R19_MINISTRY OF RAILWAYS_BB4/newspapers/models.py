from django.conf import settings
from django.db import models
from django.utils import timezone


class Preference(models.Model):
    region = (('N', 'National'),('S', 'State'),('C', 'City'))
    preference_name = models.CharField(
        max_length=1,
        choices= region,
        blank=True,
        default='N',
    )

    def __str__(self):
        return self.preference_name

class Newspaper_name(models.Model):
    preference =models.ForeignKey('Preference',on_delete=models.CASCADE,default="")
    name= models.CharField(max_length=400)
    unique_id =models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

class News(models.Model):
    heading = models.CharField(max_length=400)
    article = models.TextField()
    published_date =models.DateTimeField(blank=True,null=True)
    unique_id =models.IntegerField(blank=True,null=True)
    newspaper_name= models.ForeignKey(Newspaper_name,related_name='related_news',on_delete=models.CASCADE)

    def __str__(self):
        return self.heading
