from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255, blank=True , null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    # created_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title