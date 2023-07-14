from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=25)
    imgurl = models.CharField(max_length=300)
    blogurl = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    description = models.TextField() 

    def __str__(self): 
        return str(self.sno)+"."+self.title 
    