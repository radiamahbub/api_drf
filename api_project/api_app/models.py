from django.db import models
#from api_app.views import *

class StudentModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)
    phone = models.CharField(null=True)
