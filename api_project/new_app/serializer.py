from rest_framework import serializers
from new_app.models import *

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'
        