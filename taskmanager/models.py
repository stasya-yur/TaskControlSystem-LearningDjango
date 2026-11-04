from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "tasks")
    title = models.CharField(max_length=100)
    text = models.TextField()
    status = models.CharField(max_length=20, choices=[("TODO", "TODO"), ("InProgress", "InProgress"), ("Done", "Done")])
    priority = models.CharField(max_length=20, choices=[("Low","Low"), ("Middle", "Middle"), ("Hight","Hight")])
    deadline = models.DateTimeField()

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    date = models.DateTimeField()
