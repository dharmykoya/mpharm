from rest_framework import serializers

from .models import Diagnosis


class DiagnosisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('category_code', 'diagnosis_code', 'full_code',
                  'abbreviated_description', 'full_description', 'category_title')
