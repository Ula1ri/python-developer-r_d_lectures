from django import forms
from .models import Purchase
from book.models import Book
from user.models import User


class PurchaseForm(forms.ModelForm):
    date = forms.CharField(widget=forms.TextInput(attrs={'style': 'width 100px', 'class': 'form-control'}))
    book_id = forms.ModelChoiceField(queryset=Book.objects.all(),
                                     widget=forms.Select(attrs={'style': 'width 100px', 'class': 'form-control'}))
    user_id = forms.ModelChoiceField(queryset=User.objects.all(),
                                     widget=forms.Select(attrs={'style': 'width 100px', 'class': 'form-control'}))

    class Meta:
        model = Purchase
        fields = ('date', 'book_id', 'user_id')
