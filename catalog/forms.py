from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django import forms
import datetime

# Using forms.Form
# class RenewBookForm(forms.Form):
#     renewal_date = forms.DateField(help_text="Enter a date between noe and 4 weeks (default 3)")
#
#     def clean_renewal_date(self):
#         data = self.cleaned_data['renewal_date']
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalid date - renewal in past'))
#
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             raise ValidationError(_('Invalid date renewal more than 4 weeks ahead!'))
#
#         return data
from catalog.models import BookInstance, Book, Author

"""We can remove all this code and replace it by Model form"""


# using forms.ModelForm
class RenewBookForm(forms.ModelForm):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks")

    def clean_due_back(self):
        data = self.cleaned_data['due_back']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date renewal more than 4 weeks ahead'))

        return data

    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back': _('New renewal date')}
        help_texts = {'due_back': _('Enter a date between now and for weeks')}


choices = Author.objects.all().values_list()

choices_list = []

for item in choices:
    choices_list.append(item)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        help_texts = {
            'summery': None,
            'genre': None,
            'isbn': None
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your book title'}),
            'imprint': forms.TextInput(attrs={'class': 'form-control mt-4', 'placeholder': 'Enter imprint'}),
            'author': forms.Select(choices=choices_list, attrs={'class': 'form-control mt-2'}),
            'due_back': forms.DateField(),
            'isbn': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter ISBN'}),
            'genre': forms.CheckboxSelectMultiple(attrs={'class': 'mt-2'}),
            'summery': forms.Textarea(
                attrs={'class': 'form-control mt-4', 'placeholder': 'Enter some bio about this book'}),
        }


class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        help_texts = {
            'summery': None,
            'genre': None,
            'isbn': None
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your book title'}),
            'imprint': forms.TextInput(attrs={'class': 'form-control mt-4', 'placeholder': 'Enter imprint'}),
            'author': forms.Select(choices=choices_list, attrs={'class': 'form-control mt-2'}),
            'due_back': forms.DateField(),
            'isbn': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter ISBN'}),
            'genre': forms.CheckboxSelectMultiple(attrs={'class': 'mt-2'}),
            'summery': forms.Textarea(
                attrs={'class': 'form-control mt-4', 'placeholder': 'Enter some bio about this book'}),
        }
