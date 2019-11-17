from django.urls import path
from . import views

urlpatterns = [
    path('', views.DiagnosisListView.as_view(), name="all-diagnosis"),
    path('create', views.DiagnosisCreateView.as_view(), name="create-diagnosis"),
]
