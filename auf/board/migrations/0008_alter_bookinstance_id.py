# Generated by Django 4.0.3 on 2022-03-10 08:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_alter_bookinstance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('de179e3e-a899-49a1-9ace-bfb6ab842775'), help_text='Уникальный ID для этого экземпляра книги из целой библиотеки', primary_key=True, serialize=False),
        ),
    ]
