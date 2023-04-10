from django.shortcuts import render
from rest_framework.response import Response
from .models import studentmodel
from .serializer import studentserialzer
from rest_framework import status
from rest_framework .views import APIView

class studentapi(APIView):
 def get (self, request, pk=None, format=None):
     id =pk
     if id is not None:
      stu=studentmodel.objects.get(id=id)
      serialzer=studentserialzer(stu)
      return Response(serialzer.data)

     stu= studentmodel.objects.all()
     serialzer=studentserialzer(stu, many=True)
     return Response(serialzer.data)
     

 def post(self, request, format=None):
        serialzer=studentserialzer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({'msg':'data inserted'})
        return Response(serialzer.errors)

 def put(self, request, pk=None, format=None):   
        id = pk
        stu= studentmodel.objects.get(id)
        serialzer=studentserialzer(stu)
        if serialzer.is_valid():
            serialzer.save()
            return Response({'msg':'data inserted'})
        return Response(serialzer.errors)    
        return Response({'status':200 })

# Create your views here.
