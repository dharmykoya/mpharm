from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Diagnosis
from .serializers import DiagnosisSerializer

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


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all diagnosis added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(reverse("all-diagnosis"))

        # fetch the data from db
        expected = Diagnosis.objects.all()
        serialized = DiagnosisSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
