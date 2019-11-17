from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import DiagnosisSerializer
from .models import Diagnosis
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404


class DiagnosisAPIView(APIView):

    def get(self, request, format=None):
        diagnosis = Diagnosis.objects.all()
        serializer = DiagnosisSerializer(diagnosis, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DiagnosisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiagnosisListView(APIView):
    def get_object(self, pk):
        try:
            return Diagnosis.objects.get(pk=pk)
        except Diagnosis.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        diagnosis = self.get_object(pk)
        serializer = DiagnosisSerializer(diagnosis)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        diagnosis = self.get_object(pk)
        serializer = DiagnosisSerializer(
            diagnosis, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
