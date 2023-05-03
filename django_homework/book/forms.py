from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 300px', 'class': 'form-control'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 300px', 'class': 'form-control'}))
    year = forms.IntegerField(widget=forms.TextInput(attrs={'style': 'width: 300px', 'class': 'form-control'}))
    prise = forms.IntegerField(widget=forms.TextInput(attrs={'style': 'width: 300px', 'class': 'form-control'}))

    class Meta:
        model = Book
        fields = ('title', 'author', 'year', 'prise')