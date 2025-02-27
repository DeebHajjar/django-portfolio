from django.db import models
from django.core.validators import FileExtensionValidator

class About (models.Model):
    rule_span = models.CharField(max_length=50, default='Full Stack')
    rule = models.CharField(max_length=50, default='developer')
    about = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SocialMedia (models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Home (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cv_file = models.FileField(validators=[FileExtensionValidator(['pdf'])])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Skills (models.Model):
    skill = models.CharField(max_length=50)
    picture = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.skill


class Project (models.Model):
    title = models.CharField(max_length=100)
    short_descrition = models.CharField(max_length=255)
    descrition = models.TextField(max_length=2047)
    link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    skills = models.ManyToManyField(Skills)
    
    def __str__(self):
        return self.title


class Images (models.Model):
    Image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.project.title  + ' ' + str(self.id)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.created_at}"
    
    class Meta:
        ordering = ['-created_at']


class ProjectRating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.project.title} - {self.name} - {self.rating} stars"
    
    class Meta:
        ordering = ['-created_at']
