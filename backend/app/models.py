from django.db import models

# Create your models here.
class Post(models.Model):
    body= models.TextField(blank=False) # markdown data expected
    body_html = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.body