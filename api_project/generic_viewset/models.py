from django.db import models

# Create your models here.

class BlogModel(models.Model):
    TYPES = [
        ('Education', 'Education'),
        ('Tech', 'Tech'),
        ('Sports', 'Sports'),
    ]

    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    author = models.CharField(max_length=100, null=True)
    category = models.CharField(choices=TYPES, max_length=100, null=True)

    def __str__(self):
        return f'{self.title}'

class CourseModel(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True) 
    course_fee = models.FloatField(null=True)
    admission_end = models.DateField(auto_now_add=True)
    

    def __str__(self):
            return f'{self.title}'
    