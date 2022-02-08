from django.shortcuts import render

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
