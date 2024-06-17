from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework.views import APIView

# Create your views here.


@api_view(['GET'])
def index(request):
    students = Students.objects.all()
    serializer = Studentserializer(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addStudent(request):
    if request.method == 'POST':
        data = request.data
        serializer = Studentserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['PUT', 'PATCH'])
def updateStudent(request, pk):
    student = Students.objects.get(id=pk)
    if request.method == 'PUT':
        serializer = Studentserializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'PATCH':
        serializer = Studentserializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
class deleteStudents(APIView):
    
    
    
    def delete(self,request,pk):
        obj=Students.objects.get(id=pk)
        obj.delete()
        return Response({"message":"object deleted"})
        
