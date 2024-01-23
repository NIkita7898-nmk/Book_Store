from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from books.models import Book

class AddBookTest(APITestCase):
    fixtures = [
        "fixture/author_fixture.json",
        "fixture/book_fixture.json",
        "fixture/information_fixture.json",
    ]
    def setUp(self):
        self.url = "/book/"
        self.valid_payload = {
            "title":"Think Like a Monk",
            "publish_year":"2020",
            "author":"2",
            "barcode":"2wdc"
        }
        self.invalid_payload = {
            
            "publish_year":"2020",
            "author":"2",
            "barcode":"2wdc"
        }


    def test_add_book_view(self):
        self.client = APIClient()
        response = self.client.post(
            self.url,
            self.valid_payload
           
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_book_with_missing_title(self):
        self.client = APIClient()
        response = self.client.post(
            self.url,
           self.invalid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_non_exist_book_author(self):
        self.client = APIClient()
        response = self.client.post(
            self.url,
            {
            "title":"Think Like a Monk",
            "publish_year":"2020",
            "author":"24",
            "barcode":"2wdc"
           }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetBookTest(APITestCase):

    fixtures = [
        "fixture/author_fixture.json",
        "fixture/book_fixture.json",
        "fixture/information_fixture.json",
    ]
    def setUp(self):
        self.url = "/book/<int:pk>"
        self.client = APIClient()

    def test_add_book_view(self):
        self.client = APIClient()
        response = self.client.get(
            "/book/1/",
           
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_book_with_missing_title(self):
        response = self.client.get(
           "/book/13/",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)