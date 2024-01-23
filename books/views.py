from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from books.models import Book
from books.serializer import BookSerializer,BookByIdSerializer

# Create your views here.

class BookView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookById(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookByIdSerializer

class BookSearchView(APIView):
    def get(self, request, *args, **kwargs):
        barcode = request.GET.get('barcode')
        print(barcode)
        if not barcode:
            return Response({'error': 'Barcode parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        books = Book.objects.filter(barcode=barcode).order_by('barcode')
        serializer = BookByIdSerializer(books, many=True)

        response_data = {
            'found': len(books),
            'items': serializer.data
        }

        return Response(response_data)
