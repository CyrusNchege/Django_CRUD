from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    #ordering that we start with the last task
    class Meta:
        ordering = ['-id']
    

    def __str__(self):
        return self.title