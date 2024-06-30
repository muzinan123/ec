# -*- coding: utf-8 -*-
# @Time: 2/19 17:12
# @DESC:
from django.urls import path
from .views import *

urlpatterns = [
    path("svc_data/", SvcDataView.as_view()),
]
