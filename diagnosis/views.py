from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import DiagnosisSerializer
from .models import Diagnosis

from rest_framework import generics, status
from rest_framework.response import Response


class DiagnosisListView(generics.ListAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
