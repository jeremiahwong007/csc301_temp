from django.urls import path
from views import CreateTrialData

urlpatterns = [
    path('data/save/', CreateTrialData.as_view())
]