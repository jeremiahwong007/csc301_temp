from django.urls import path
from django.urls import path, include
from api.views import (
    CreateBreathingDataView,
    ListBreathingDataView,
    RetrieveBreathingDataView
)

urlpatterns = [
    path('data/create/', CreateBreathingDataView.as_view()),
    path('data/all', ListBreathingDataView.as_view()),
    path('data/<int:pk>', RetrieveBreathingDataView.as_view()),
]