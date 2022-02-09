from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from catalog.models import *


def home(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()

    num_genders = Genre.objects.all().count()
    genders_type = Genre.objects.filter(name__exact='Action').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genders': num_genders,
        'genders_type': genders_type
    }

    return render(request, 'catalog/home.html', context=context)


class BookList(ListView):
    model = Book
    context_object_name = 'my_books'  # this context we use it in template for loop-in
    queryset = Book.objects.filter(title__icontains="book")[:5]
    template_name = 'catalog/list_books.html'


class BookDetail(DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'


# def book_detail(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         raise Http404('Book does not exist')
#
#     return render(request, 'catalog/book_detail.html', context={'book': book})
