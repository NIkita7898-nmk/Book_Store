from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from authors.models import Author

class AddAuthorTest(APITestCase):
    fixtures = [
        "fixture/author_fixture.json",
        "fixture/book_fixture.json",
        "fixture/information_fixture.json",
    ]
    def setUp(self):
        self.url = "/author/"
        self.valid_payload = {
            "name":"Jay Shetty",
            "birth_date":"1987-09-06"
        }
        self.invalid_payload = {
               "birth_date":"1987-09-06"
          
        }

    def test_add_author_view(self):
        self.client = APIClient()
        response = self.client.post(
            self.url,
            self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_view_with_missing_name(self):
        self.client = APIClient()
        response = self.client.post(
            self.url,
           self.invalid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      
class GetAuthorTest(APITestCase):
    
    fixtures = [
        "fixture/author_fixture.json",
        "fixture/book_fixture.json",
        "fixture/information_fixture.json",
    ]
    def setUp(self):
        self.url = "/author/<int:pk>"
        self.client = APIClient()

    def test_get_author_view(self):
        self.client = APIClient()
        response = self.client.get(
            "/author/1/",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_non_exist_author(self):
        response = self.client.get(
           "/author/13/",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)