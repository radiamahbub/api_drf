#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api_app.models import *
from api_app.serializers import *


@api_view(['GET', 'POST'])
def student_list(req):
    if req.method == 'GET':

        student_data = StudentModel.objects.all()

        serializer_data = StudentSerializer(student_data, many=True)

        return Response({
            'success':True,
            'message':'Successfully achieved Student Information.',
            'data':serializer_data.data
        }, status=status.HTTP_200_OK)

    if req.method == 'POST':

        serializer_data = StudentSerializer(data = req.data)

        if serializer_data.is_valid():

            serializer_data.save()

            return Response({
            'success':True,
            'message':'Successfully created Student Information.',
            'data':serializer_data.data
        }, status=status.HTTP_200_OK)

        return Response({
            'success':True,
            'message': serializer_data.errors
        })

@api_view (['GET','PUT', 'DELETE'])
def student_details(req, id):
    try:
        student = StudentModel.objects.get(id = id)
    except:
        return Response({
            'success':False,
            'message':'Data not found'
        }, status=status.HTTP_404_NOT_FOUND)    

    if req.method == 'GET':
        serializer_data = StudentSerializer(student)

        return Response({
            'success':True,
            'message':'Successfully created Student Information.',
            'data':serializer_data.data
        }, status=status.HTTP_200_OK)

    elif req.method == 'DELETE':
        student.detete()
        return Response({
                    'success':False,
                    'message':'Student info Deleted.'
                }) 
    elif req.method == 'PUT':
        serializer_data = StudentSerializer(student, data = req.data)
        if serializer_data.is_valid():
            serializer_data.save()

            return Response({
                'success':False,
                'message':'Successfully updated Student Information.',
                'data': serializer_data.data
            }, status=status.HTTP_201_CREATED) 
