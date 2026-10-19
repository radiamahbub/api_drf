from django.urls import path, include
from generic_viewset.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('blog_list/', BlogListAPI.as_view()),
    path('blog_get/<str:pk>/', BlogGetAPI.as_view()),
    path('blog_all/<str:pk>/', BlogIndividual.as_view()),
    path('', include(router.urls))
]