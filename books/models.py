from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField
    author_title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
