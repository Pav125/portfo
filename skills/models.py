from django.db import models

# Create your models here.
class Profile(models.Model):
    image = models.ImageField(null=True, blank=True,upload_to='images/')
    # github_logo = models.ImageField(null=True, blank=True,upload_to='github_logo/')
    # linkedin_logo = models.ImageField(null=True, blank=True,upload_to='linkedin_logo/')

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to='project_images')
    link = models.URLField()

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    skill = models.CharField(max_length=100)

    def __str__(self):
        return self.skill
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200,null=True,blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name