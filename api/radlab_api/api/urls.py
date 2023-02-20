<<<<<<< HEAD
from django.urls import path, include
from api.views import (
    ListBreathingDataView,
    RetrieveBreathingDataView
)

urlpatterns = [
    path('data/all', ListBreathingDataView.as_view()),
    path('data/<int:pk>', RetrieveBreathingDataView.as_view()),
=======
from django.urls import path
from views import CreateTrialData

urlpatterns = [
    path('data/save/', CreateTrialData.as_view())
>>>>>>> 19ed793c532a7807fdc0addcd879e9ff2f70c2ee
]