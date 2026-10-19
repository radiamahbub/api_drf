from django.db import models

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

