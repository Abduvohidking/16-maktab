from django.db import models

# Create your models here.
class kitob(models.Model):
    title=models.CharField(max_length=300)
    author_name=models.CharField(max_length=300)
    photo = models.ImageField(upload_to='%Y%m%d')
    file = models.FileField(blank=True)
    categories = models.CharField(max_length=200)
    content = models.TextField(blank=True,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True ,blank=True,null=True)
    def __str__(self):
        return  self.title


class audio_kitob(models.Model):
    title=models.CharField(max_length=300)
    author_name=models.CharField(max_length=300)
    photo = models.ImageField(upload_to='%Y%m%d')
    audio = models.ManyToManyField('audio',null=True,blank=True)
    categories = models.CharField(max_length=200 ,default='audio_kitob')
    content = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True ,blank=True)
    def __str__(self):
        return  self.title
class audio(models.Model):
    title = models.CharField(max_length=300)
    audio=models.FileField(blank=True)
    def __str__(self):
        return self.title