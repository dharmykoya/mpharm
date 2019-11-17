from django.urls import path
from . import views

urlpatterns = [
    path('diagnosis', views.DiagnosisAPIView.as_view(), name="diagnosis"),
    path('diagnosis/<int:pk>', views.DiagnosisListView.as_view(),
         name="diagnosis-detail"),
]
