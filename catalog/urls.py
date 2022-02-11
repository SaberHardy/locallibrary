from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book_list/', views.BookList.as_view(), name='book_list'),
    path('book_detail/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    # path('book_detail/<int:pk>/', views.book_detail, name='book_detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='mybooks'),
    path('book/<uuid:pk>/renew/', views.renew_book, name='renew_book'),

    path('author/create/', views.AuthorCreate.as_view(), name='create_author'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='update_author'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='delete_author'),


    path('book/create/', views.BookCreate.as_view(), name='book_create'),

]
