from django.db import models

# Create your models here.

class Post(models.Model):
    title  = models.CharField(max_length=150)
    authur_name = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    