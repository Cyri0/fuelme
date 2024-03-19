from django.urls import path
from . import views

# http://localhost:8000/refuels/all/

urlpatterns = [
    path('all/', views.getAllRefuels),
    path('consumption/', views.getLastConsumption)
]