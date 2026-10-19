from django.urls import path
from new_app.views import *

urlpatterns = [
    path('blog', BlogAPIView.as_view()),
    path('blog_details/<int:id>/', BlogDetails.as_view()),
]