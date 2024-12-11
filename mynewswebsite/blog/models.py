
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(("1",'Active'), ("2",'Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default="")
    title = models.TextField()
    short_description = models.TextField()
    content = models.TextField()
    banner_path = models.ImageField(upload_to='news_bannner')
    status= models.BooleanField(("staff status"),default=False,null=True)
    meta_keywords = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)
    slug = models.SlugField(default="", null=False , unique=True)
    seotitle = models.TextField(default="")
    seo_description= models.TextField(default="")
    seo_script= models.TextField(default="")

    

    def __str__(self):
        return f"{self.user.username} - {self.title} -{self.status}"





