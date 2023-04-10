from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import studentmodel
from .serializer import studentserialzer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
     id =pk
     if id is not None:
      stu=studentmodel.objects.get(id=id)
      serialzer=studentserialzer(stu)
      return Response(serialzer.data)

     stu= studentmodel.objects.all()
     serialzer=studentserialzer(stu, many=True)
     return Response(serialzer.data)
     

    if request.method=='POST':
        serialzer=studentserialzer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({'msg':'data inserted'})
        return Response(serialzer.errors)

    if request.method=='PUT':
        id = pk
        stu= studentmodel.objects.get(id)
        serialzer=studentserialzer(stu)
        if serialzer.is_valid():
            serialzer.save()
            return Response({'msg':'data inserted'})
        return Response(serialzer.errors)    
    return Response({'status':200 })      
auth=[BasicAuthentication]
per=[IsAuthenticated]


# Create your views here.
