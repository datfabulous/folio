from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='portfolio/profile/')

    def __str__(self):
        return self.name


