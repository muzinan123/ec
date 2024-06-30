# -*- coding: utf-8 -*-
# @Time: 2/19 17:12
# @DESC:
from django.urls import path
from .views import *

urlpatterns = [
    path("node/<str:name>/", MetricsNodeView.as_view()),
    path("pod/<str:namespace>/<str:name>/", MetricsPodView.as_view())
]
