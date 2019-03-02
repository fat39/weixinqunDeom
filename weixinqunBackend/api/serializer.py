# -*- coding:utf-8 -*-
from wxqInfo import models
from rest_framework import serializers

class QunInfoModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.QunInfo
        fields = '__all__'