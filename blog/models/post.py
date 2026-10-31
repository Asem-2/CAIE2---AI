from django.db import models

# Create your models here.
class Post(models.Model):
    title_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title