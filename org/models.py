from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField
#from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title= models.CharField(max_length=250)
    College= models.CharField(max_length=250)
    #content=CKEditor5Field('Text', config_name='extends')
    content= RichTextField()
    venue= models.CharField(max_length=100)
    connect=models.CharField(max_length=500)
    timeStamp=models.DateTimeField(blank=True)
    #slug=models.CharField(max_length=130)
    slug = models.SlugField(unique=True)
    registerurl = models.URLField(max_length=200)
    reachurl = models.URLField(max_length=200)
    image=models.FileField(upload_to="org/",max_length=250)
    
    def __str__ (self):
        return self.title + ' at ' + self.College
    
class orgcomment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True )
    timeStamp=models.DateTimeField(default=now)
    
    def __str__(self):
        return self.comment[0:13] + "...." + " by " + self.user.username
    
        
    
    