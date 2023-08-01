from django.db import models

class TaskModel(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)