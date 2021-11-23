from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    name_text = models.CharField(max_length=200)
    desc_text = models.CharField(max_length=200)
    proj_text = models.CharField(max_length=200)
    status    = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.id}: {self.name_text}"

    def get_absolute_url(self):
        return reverse('task-url', kwargs{ 'pk' : self.pk)

'''class TimeEntry(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time   = models.DateTimeField()
    
    def __str__(self):
        return f"{self.id}: {self.start_time} {self.end_time}"'''
        
