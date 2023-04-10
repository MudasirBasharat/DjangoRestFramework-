from .models import studentmodel
from .serilzer import studentserialzer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,DestroyModelMixin

class studentlist(GenericAPIView,ListModelMixin):
    queryset= studentmodel.objects.all()
    serializer_class=studentserialzer

    def get(self,request, *arg, **kwargs):
        return self.list(request, *arg, **kwargs)

class studentcreate(GenericAPIView, CreateModelMixin):
    queryset= studentmodel.objects.all()
    serializer_class=studentserialzer

    def post(self,request, *arg, **kwargs):
        return self.create(request, *arg, **kwargs)

class studentretrive(GenericAPIView,RetrieveModelMixin):
    queryset= studentmodel.objects.all()
    serializer_class=studentserialzer

    def get(self,request, *arg, **kwargs):
        return self.retrieve(request, *arg, **kwargs)        
