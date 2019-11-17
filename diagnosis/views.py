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


class DiagnosisCreateView(generics.CreateAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer

    def create(self, request, *args, **kwargs):
        super(DiagnosisCreateView, self).create(request, args, kwargs)

        # response = {
        #     "message": "Successfully created",
        #     "result": request.data}
        # return Response(data=response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            super(DiagnosisCreateView, self).create(request, args, kwargs)

            response = {
                "message": "Successfully created",
                "result": request.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
