from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employer(models.Model):
    name = models.CharField(unique=True, max_length=300)
    website = models.URLField(blank=True)
    location = models.CharField(max_length = 255)

class Job(models.Model):
    title = models.CharField(unique=True, max_length=300)

class Employment(models.Model):
    employee = models.ForeignKey(User)
    employer = models.ForeignKey(Employer)
    job = models.ForeignKey(Job)
    begin = models.DateField()
    end = models.DateField(blank=True)

class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    employment = models.ForeignKey(Employment)

class SkillCategory(models.Model):
    name = models.CharField(max_length=300)

class Skill(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(SkillCategory)
    description = models.TextField(blank=True)

class TaskSkillSet(models.Model):
    skill = models.ForeignKey(Skill)
    task = models.ForeignKey(Task)
    full = models.BooleanField(default=True)

class Profile(models.Model):
    user = models.OneToOneField(User)
    strengths = models.ManyToManyField(Skill)
    description = models.TextField()
    hireme_date = models.DateField()
