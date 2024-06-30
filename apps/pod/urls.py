# -*- coding: utf-8 -*-
# @Time: 2/19 17:12
# @DESC:
from django.urls import path
from .views import *

urlpatterns = [
    path("pod/", PodView.as_view()),
    path("pod/<str:namespace>/", PodView.as_view()),
    path("pod/<str:namespace>/<str:name>/", PodView.as_view()),
    path("pod/<str:node_name>/",PodView.as_view())
]
