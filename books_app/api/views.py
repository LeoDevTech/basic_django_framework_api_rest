from rest_framework import status

from .serializers import BookSerializer
from ..models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        obj_serializer = BookSerializer(data=request.data)
        if obj_serializer.is_valid():
            obj_serializer.save()
            return Response(obj_serializer.data)
        else:
            return Response(obj_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def book_search(request, pk):
    if request.method == 'GET':
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({'msg': 'Do not exist Item'}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        try:
            book = Book.objects.get(pk=pk)
            obj_serializer = BookSerializer(book, data=request.data)
            if obj_serializer.is_valid():
                obj_serializer.save()
                return Response(obj_serializer.data)
            else:
                return Response(obj_serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Book.DoesNotExist:
            return Response({'msg': 'Book doesn\'t exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({'msg': 'Book doesn\'t exist'}, status=status.HTTP_404_NOT_FOUND)








