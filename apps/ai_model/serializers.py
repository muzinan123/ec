# -*- coding: utf-8 -*-
# @Time: 3/5 16:09
# @DESC:
from .models import *
from rest_framework import serializers


class AiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiModel
        fields = ['version', "class_names", "filename", "file_md5", "file_path"]
