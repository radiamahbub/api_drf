from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from generic_viewset.serializers import *
from generic_viewset.models import *


class BlogListAPI(generics.ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class BlogGetAPI(generics.RetrieveAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class BlogIndividual(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


class CourseViewSet(ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer