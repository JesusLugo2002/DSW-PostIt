from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    checked = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title    