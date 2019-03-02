from django.shortcuts import render
from django.views import View
from . import serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from wxqInfo import models as wxqInfo_models

class qunInfoApi(APIView):

    def get(self, request, *args, **kwargs):
        qun_list = wxqInfo_models.QunInfo.objects.all()
        qs = serializer.QunInfoModelSerializers(qun_list, many=True, context={"request": request})
        return Response(qs.data)

    def post(self,request):
        qunInfo = serializer.QunInfoModelSerializers(data=request.data)
        if qunInfo.is_valid():
            qunInfo.save()
            return Response(qunInfo.data)
        return Response(qunInfo.errors)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(qunInfoApi, self).dispatch(request, *args, **kwargs)


