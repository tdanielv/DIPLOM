from django import forms
from wtforms import Form, StringField, SelectField

# class SearchForm(Form):
#     choices = [('title', 'Название'),
#     ('genre', 'Жанр'),
#     ('author', 'Автор'),
#     ('description', 'Описание') ,
#     ('price', 'Цена') ]
#     select = SelectField('Поиск книг по:', choices=choices)
#     search = StringField('')
#
# class SearchForm(forms.ModelForm):
#     title = forms.Charfield(max_length = 200)



class SearchForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label='Название')
