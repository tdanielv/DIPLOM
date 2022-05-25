# Generated by Django 4.0.3 on 2022-03-09 08:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_bookinstance_options_bookinstance_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d30df54d-3176-4cf4-b59f-4e9cfc5e4063'), help_text='Уникальный ID для этого экземпляра книги из целой библиотеки', primary_key=True, serialize=False),
        ),
    ]
