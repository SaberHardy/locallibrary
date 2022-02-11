import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import RenewBookForm, BookForm
from catalog.models import *


def home(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()

    num_genders = Genre.objects.all().count()
    genders_type = Genre.objects.filter(name__exact='Action').count()

    """Starting with sessions"""
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genders': num_genders,
        'genders_type': genders_type,
        'num_visits': num_visits
    }

    return render(request, 'catalog/home.html', context=context)


class BookList(ListView):
    model = Book
    context_object_name = 'my_books'  # this context we use it in template for loop-in
    queryset = Book.objects.filter(title__icontains="book")
    template_name = 'catalog/list_books.html'
    paginate_by = 5


class BookDetail(DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'


class AuthorListView(ListView):
    model = Author
    template_name = 'catalog/all_authors.html'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'catalog/author_detail.html'


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/book_instance_borrowed.html'

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user) \
            .filter(status__exact='o').order_by('due_back')


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == "POST":
        form = RenewBookForm(request.POST)

        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()
            return HttpResponseRedirect(reverse('mybooks'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew.html', context)


class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/09/2021'}


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'catalog/book_form.html'
    # fields = '__all__'
