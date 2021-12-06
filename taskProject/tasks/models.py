from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    proj = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('tasks:single', args=[self.id])
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class TimeEntry(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time   = models.DateTimeField()
    
    def __str__(self):
        return f"{self.id}: {self.start_time} {self.end_time}