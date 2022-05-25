from django import forms
from django.core.exceptions import ValidationError

from .models import Books, Author, Genre, Year


class AddGenreForm(forms.ModelForm):
    genre = forms.CharField(max_length=100, label='Введите жанр')
    class Meta:
        model = Genre
        fields = '__all__'

class AddYearForm(forms.ModelForm):
    year = forms.CharField(max_length=100, label='Введите год')
    class Meta:
        model = Year
        fields = '__all__'

class AddAuthorForm(forms.ModelForm):
    author = forms.CharField(max_length=100, label='Введите автора')
    class Meta:
        model = Author
        fields = '__all__'

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

    def clean(self):
        super().clean()
        errors = {}
        if not self.cleaned_data['description']:
            errors['description'] = ValidationError('Укажите описание')
        if self.cleaned_data['price'] < 0:
            errors['price'] = ValidationError('Укажите неотрицательное значение')

        if errors:
            raise ValidationError(errors)

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100)