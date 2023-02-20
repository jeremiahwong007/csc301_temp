from django.urls import path, include
from api.views import (
    ListBreathingDataView,
    RetrieveBreathingDataView
)

urlpatterns = [
    path('data/all', ListBreathingDataView.as_view()),
    path('data/<int:pk>', RetrieveBreathingDataView.as_view()),
]