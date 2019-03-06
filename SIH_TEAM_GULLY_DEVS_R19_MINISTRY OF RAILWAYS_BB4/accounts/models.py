from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from newspapers.models import Newspaper_name,Preference

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete="models.CASCADE")
    name = models.CharField(max_length=30, blank=True)
    email_id = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    #bio = models.TextField(max_length=500, blank=True)
    phone_number = models.IntegerField(blank=True ,null=True)
    birth_date = models.DateField(null=True, blank=True)
    service_number = models.IntegerField(blank=True ,null=True)
    designation = models.CharField(max_length=30, blank=True)
    railway_zone = models.CharField(max_length=30, blank=True)
    
    picture = models.ImageField(upload_to = 'profile_pics')
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unsure',),
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Favourites(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    newspaper_name=models.OneToOneField(Newspaper_name, on_delete=models.CASCADE)
