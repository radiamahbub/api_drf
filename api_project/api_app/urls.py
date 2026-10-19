from django.urls import path
from api_app.views import *

urlpatterns = [
    path('', student_list, name='student'),
    #path('student_details/<int:1>/', student_details, name='student_details'),
    # path('', student, name='student'),
    # path('', student, name='student'),
]