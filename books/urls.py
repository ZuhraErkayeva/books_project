from django.urls import path
from . import views
app_name = 'books'
urlpatterns = [
    path('book',views.books_list,name='book_list'),
    path('books/<int:pk>', views.book_detail, name='book_detail'),
]