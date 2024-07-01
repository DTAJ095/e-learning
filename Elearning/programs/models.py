from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Niveaux(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()


    def __str__(self):
        return self.nom


    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)  
        super().save(*args, **kwargs)  

class Courses(models.Model):
    course_id= models.CharField(max_length=50)
    title= models.CharField(max_length=100)
    description= models.TextField(User)
    instructeur= models.CharField(User, max_length=40)

class Lesson(models.Model):
    lesson_id= models.CharField(max_length=10)
    course_id= models.ForeignKey(Courses, verbose_name=(""), on_delete=models.CASCADE)
    title= models.CharField(max_length=50)
    description= models.CharField(max_length=500)

class Ressource(models.Model):
    ressource_id=models.CharField(max_length=50)
    lesson_id=models.ForeignKey(Lesson, verbose_name=(""), on_delete=models.CASCADE)
    title= models.CharField(max_length=50)
    #format des fichiers
    video ='video'
    pdf= 'pdf'
    fpp='fpp'
    typeformat={
        (video ,'video'),(pdf, 'pdf'),(fpp, 'fpp')
    }
    format_r= models.CharField(choices=typeformat, max_length=50)
    ressource= models.FileField(upload_to="Media", max_length=100) 

class Formation(models.Model):
    formation_id= models.CharField(max_length=50)
    tutorat=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    date_start=models.DateField(auto_now=True, auto_now_add=False)
    date_end= models.DateField(auto_now=True, auto_now_add=False)
