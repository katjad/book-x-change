from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def loan_item(self, request, pk=None):
        book = self.get_object()
        book.loan_item(book, request.data['holder'])
        if book.save():
            return Response(
                {
                    'status': book.status,
                }
            )
        return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def request_item(self, request, pk=None):
        book = self.get_object()
        book.request_item(book, request.data['holder'])
        if book.save():
            return Response(
                {
                    'status': book.status,
                }
            )
        return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def return_item(self, request, pk=None):
        book = self.get_object()
        book.return_item(book, request.data['holder'])
        if book.save():
            return Response(
                {
                    'status': book.status,
                }
            )
        return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)
