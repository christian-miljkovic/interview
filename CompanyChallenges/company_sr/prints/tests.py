from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Prints, Order
from .serializers import PrintsSerializer, OrdersSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_print(size=""):
        if size != "":
            if size == "S":
                Prints.objects.create(size=size, cost="10.00", shipping_cost="4.99", total_cost="14.99")
            elif size == "M":
                Prints.objects.create(size=size, cost="15.00", shipping_cost="5.99", total_cost="20.99")
            elif size == "L":
                Prints.objects.create(size=size, cost="20.00", shipping_cost="7.99", total_cost="27.99")

    @staticmethod
    def create_order(first_name="", address_one=""):        
        if first_name and address_one:
            Order.objects.create(first_name=first_name, 
                                last_name="Test", email=first_name.lower() + "@gmail.com", phone_number="203-900-8179", address_one=address_one,
                                address_two="#3", city="NY", state="NY", postal_code="10011", country="US")
        

    def setUp(self):
        # add test data
        self.create_print("S")
        self.create_print("M")
        self.create_print("L")
        self.create_order("Alice","274 3rd Street")
        self.create_order("Bob", "372 4th Street")
        

class GetAllPrints(BaseViewTest):

    def test_get_all(self):
        """
        This test ensures that all prints added in the setUp method
        exist when we make a GET request to the prints/ endpoint
        """
        # hit the API endpoint
        prints_response = self.client.get(
            reverse("prints-all", kwargs={"version": "v1"})
        )

        order_response = self.client.get(
            reverse("orders-all", kwargs={"version": "v1"})
        )

        # fetch the data from db for the prints test
        expected_prints = Prints.objects.all()
        serialized_print = PrintsSerializer(expected_prints, many=True)
        self.assertEqual(prints_response.data, serialized_print.data)
        self.assertEqual(prints_response.status_code, status.HTTP_200_OK)

        # fetch the data from db for the order test
        expected_orders = Order.objects.all()
        serialized_order = OrdersSerializer(expected_orders, many=True)
        self.assertEqual(order_response.data, serialized_order.data)
        self.assertEqual(order_response.status_code, status.HTTP_200_OK)