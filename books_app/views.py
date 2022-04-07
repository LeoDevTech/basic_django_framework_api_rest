# from django.http import JsonResponse
# from django.shortcuts import render
# from books_app.models import Book
#
#
# def book_list(request):
#     books = Book.objects.all()
#     data = {
#         'books': list(books.values())
#     }
#     return JsonResponse(data)
#
#
# def book_search(request, pk):
#     book = Book.objects.get(pk)
#     data = {
#         'name': book.name,
#         'author': book.author,
#         'description': book.description,
#         'stock': book.stock,
#     }
#     return JsonResponse(data)
