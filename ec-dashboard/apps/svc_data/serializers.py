# -*- coding: utf-8 -*-
# @Time: 3/6 21:41
# @DESC:
from .models import SvcData
from rest_framework import serializers


class SvcDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SvcData
        fields = ['image_base64', 'detect_result','upload_time']
