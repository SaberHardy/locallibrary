from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book_list/', views.BookList.as_view(), name='book_list'),
    path('book_detail/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    # path('book_detail/<int:pk>/', views.book_detail, name='book_detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
]
