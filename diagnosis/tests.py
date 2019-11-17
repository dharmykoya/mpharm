from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Diagnosis
from .serializers import DiagnosisSerializer
import json

# Create your tests here.


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_diagnosis(category_code="", diagnosis_code="", full_code="", abbreviated_description="", full_description="", category_title=""):
        if category_code != "" and diagnosis_code != "":
            Diagnosis.objects.create(category_code=category_code, diagnosis_code=diagnosis_code, full_code=full_code,
                                     abbreviated_description=abbreviated_description, full_description=full_description, category_title=category_title)

    def setUp(self):
        # add test data
        self.create_diagnosis("A002", "01", "0012",
                              "malaria typhoid", "malaria", "malaria")
        self.create_diagnosis("A012", "67", "0067",
                              "malaria bacteria", "malaria", "malaria")
        self.create_diagnosis("A032", "43", "0043", "hiv", "hiv aids", "aids")
        self.create_diagnosis("A042", "31", "0031",
                              "malaria", "malaria virus", "malaria")

    def test_get_all_diagnosis(self):
        """
        This test ensures that all diagnosis added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(reverse("diagnosis"))

        # fetch the data from db
        expected = Diagnosis.objects.all()
        serialized = DiagnosisSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_diagnosis(self):
        """
        This test ensures that a new diagnosis is added to the db with a POST request
        """
        # hit the API endpoint
        params = {
            "category_code": "A049",
            "diagnosis_code": "0867",
            "full_code": "A084222",
            "abbreviated_description": "cough",
            "full_description": "cold and cough",
            "category_title": "cold"
        }
        response = self.client.post(reverse("diagnosis"), params)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_field(self):
        """
        This test ensures that aan error is thrown when an empty field is passed in
        """
        # hit the API endpoint
        params = {
            "category_code": "A049",
            "diagnosis_code": "0867",
            "full_code": "A084222",
            "abbreviated_description": "cough",
            "full_description": "cold and cough",
            "category_title": ""
        }

        response = self.client.post(reverse("diagnosis"), params)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_update_diagnosis(self):
        """
        This test ensures that a diagnosis detail is updated
        """
        diagnosis = Diagnosis.objects.create(category_code="A002", diagnosis_code="01", full_code="0012",
                                             abbreviated_description="malaria typhoid", full_description="malaria", category_title="malaria")
        params = {
            "full_description": "cold and cough with bacteria",
        }
        response = self.client.patch(
            reverse('diagnosis-detail', kwargs={'pk': diagnosis.id}), params
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["full_description"], params["full_description"])

    def test_invalid_update_diagnosis_(self):
        """
        This test ensures that an error is thrown for a diagnosis not found
        """
        params = {
            "full_description": "cold and cough with bacteria",
        }
        response = self.client.patch(
            reverse('diagnosis-detail', kwargs={'pk': 1000}), params
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
