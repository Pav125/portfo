from django.contrib import admin
from .models import Profile, Project, Skill, Contact

# Register your models here.

admin.site.register(Profile)

admin.site.register(Project)

admin.site.register(Skill)

admin.site.register(Contact)