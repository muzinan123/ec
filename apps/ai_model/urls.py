# -*- coding: utf-8 -*-
# @Time: 2/19 17:12
# @DESC:
from django.urls import path
from .views import *

urlpatterns = [
    path("ai_model/", AiModelView.as_view()),
    path("ai_model/<str:version>/", AiModelView.as_view()),
    path("distribute/", DistributeAiModelView.as_view()),
    path("distribute/<str:serialize_id>/", DistributeAiModelView.as_view()),

]
