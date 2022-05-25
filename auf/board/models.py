import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import date


class Books(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    year = models.ForeignKey('Year', on_delete=models.PROTECT)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    created = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='images', blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    CONDITION = (
        ( 'Ough', '0'),
        ( 'Very bad', '1'),
        ( 'Bad', '2'),
        ( 'Normal', '3'),
        ( 'Not so bad', '4'),
        ( 'Like new', '5'),
    )
    condition = models.CharField(max_length=20, choices=CONDITION, default='3')
    price = models.IntegerField(default=100)
    quantitty = models.IntegerField(default=1)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_view', args=[str(self.id)])

    class Meta:
        verbose_name = ' Экземпляр книги'
        verbose_name_plural = 'Книги'

class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre

    def get_absolut_url(self):
        return reverse('author_detail', args = [str(self.id)])

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Year(models.Model):
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.year


class Author(models.Model):
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), help_text='Уникальный ID для этого экземпляра книги из целой библиотеки')
    book = models.ForeignKey('Books', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'На обслуживании'),
        ('o', 'Взаймы'),
        ('a', 'Доступно'),
        ('r', 'Зарезервировано'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Доступность книги')
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return '%s (%s)' %(self.id, self.book.title)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
