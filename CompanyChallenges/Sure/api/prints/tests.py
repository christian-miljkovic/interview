from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Prints
from .serializers import PrintsSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_print(size=""):
        if size != "":
            if size == "S":
                Songs.objects.create(size=size, cost="10.00", shipping_cost="4.99", total_cost="14.99")
            elif size == "M":
                Songs.objects.create(size=size, cost="15.00", shipping_cost="5.99", total_cost="20.99")
            elif size == "L":
                Songs.objects.create(size=size, cost="20.00", shipping_cost="7.99", total_cost="27.99")

    def setUp(self):
        # add test data
        self.create_print("S")
        self.create_print("M")
        self.create_print("L")
        

class GetAllPrints(BaseViewTest):

    def test_get_all_prints(self):
        """
        This test ensures that all prints added in the setUp method
        exist when we make a GET request to the prints/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("prints-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Prints.objects.all()
        serialized = PrintsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)