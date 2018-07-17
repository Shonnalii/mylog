from django.db import models
import datetime

class Blog(models.Model):
    title=models.CharField(max_length=200,default='MyBlog')
    body=models.CharField(max_length=20000)
    tag_id = models.IntegerField(max_length=200,default='1')
    publish_draft=models.BooleanField(default=False)
    timestamp=models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-id"]
    class Admin:
        pass

class Tag(models.Model):
    tag_name=models.CharField(max_length=200)
    tag_desc=models.CharField(max_length=200)
    tag_value=models.IntegerField(default=1)




class BlogTag (models.Model):
   blog=models.ForeignKey(Blog,on_delete=models.CASCADE,default=1)
   tag=models.ForeignKey(Tag,on_delete=models.CASCADE,default=1)
#Create your models here.
