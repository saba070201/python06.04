from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title=models.CharField(max_length=150)
    prememo=models.TextField(null=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='articleapp/images',null=True,blank=True)
    date_published=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)+'__'+self.title
# Create your models here.
