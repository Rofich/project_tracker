from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    REQUIRED_FIELDS = ['']

class Project(models.Model):
    STATUS_CHOICES = [
		(1, 'В разработке'),
		(2, 'Завершен'),
		(3, 'Прекратил разработку')
	]
    name= models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    def get_status(self):
        return self.STATUS_CHOICES[self.status-1][1]
    
class ProjectUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
class Task(models.Model):
    STATUS_CHOICES = [
		(1,'в разработке'),
		(2, 'Истекли сроки'),
		(3, 'Завершен')
	]
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    end_time = models.DateTimeField()
    status = models.IntegerField(choices=STATUS_CHOICES)