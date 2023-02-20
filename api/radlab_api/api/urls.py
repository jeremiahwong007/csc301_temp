# todo/todo_api/urls.py : API urls.py
from django.conf.urls import url
from django.urls import path, include
from api.views import (
    ListBreathingDataView,
    RetrieveBreathingDataView
)

urlpatterns = [
    path('api/data/all', ListBreathingDataView.as_view()),
    path('api/data/<int:pk>', RetrieveBreathingDataView.as_view()),
]