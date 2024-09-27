from django.shortcuts import render,get_object_or_404

from .models import Book

def add_book(request):
    return render(request, 'add_book.html')

def books_list(request):
    books = Book.objects.all()
    ctx = {'books': books}
    return render(request,'book_list.html',ctx)
def book_detail(request,pk):
    books = get_object_or_404(Book,pk=pk)
    ctx = {'books': books}
    return render(request,'book_detail.html',ctx)
