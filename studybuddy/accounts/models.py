from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
class Course(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    coursename = models.CharField(max_length=200)
