from django.db import models
from django.contrib.auth.models import User
import os


def renommer_image(instance, filename):
    upload_to = 'image/'
    #pho.png
    ext = filename.split('.')[-1]
    if instance.user.username:
        filename = "photo_p/{}.{}".format(instance.user.username, ext)
    return os.path.join(upload_to, filename)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    photo_p = models.ImageField(upload_to=renommer_image, blank=True)

    Apprenant = 'Apprenant'
    Instructeur = 'instructeur'

    type_user = [
        (Apprenant, 'Apprenant'),( Instructeur, 'Instructeur')
    ]

    type_p = models.CharField(max_length=100, choices=type_user, default=Apprenant)


    def __str__(self):
        return self.user.username
