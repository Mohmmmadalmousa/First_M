from django.db import models

# Create your models here.
class Post(models.Model):
    title_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=200,unique=True)
    email = models.EmailField(max_length=200,unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username

class Category(models.Model):
    name=models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
def __str__(self):
       return self.content
