from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from new_app.serializer import *
from new_app.models import *

class BlogAPIView(APIView):
    def get(self, request):
        blog_data = BlogModel.objects.all()
        serializer_data = BlogSerializer(blog_data, many=True)
        return Response({
            'success':True,
            'message':'Data found',
            'data': serializer_data.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
            serializer_data = BlogSerializer(data = request.data)
            if serializer_data.is_valid():
                 serializer_data.save()
                 return Response({
                     'success':True,
                     'message':'Blog created sccessfully',
                     'data': serializer_data.data
                 }, status=status.HTTP_200_OK)
            else:
                return Response({
                     'success':True,
                     'message': serializer_data.errors
                })

class BlogDetails(APIView):
     
     def get_object(self, id):
          try:
               data = get_object_or_404(BlogModel, id=id)
          except BlogModel.DoesNotExist:
               return Response({
                    'success':True,
                    'message':'Data not found',
                    'data': []
                }, status=status.HTTP_200_OK)

     def get(self, request, id):
          blog_data = self.get_object(id)
          serializer_data = BlogSerializer(blog_data)
          return Response({
               'success': True,
               'message':'Blog got.',
               'data': serializer_data.data
          })    
     def delete(self, request, id):
          self.get_object(id).delete()
          return Response({
               'success': True,
               'message':'Blog deleted.',
               'data': []
          })

     def put(self, request, id):
          blog_data = self.get_object(id)
          serializer_data = BlogSerializer(blog_data, data = request.data)
          if serializer_data.is_valid():
               serializer_data.save()
               return Response({
                    'success': True,
                    'message':'Blog got.',
                    'data': serializer_data.data
               }) 
          else:
               return Response({
                    'success': True,
                    'message':serializer_data.errors
               }) 

                            
            
    
