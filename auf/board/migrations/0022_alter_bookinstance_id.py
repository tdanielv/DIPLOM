# Generated by Django 4.0.3 on 2022-03-17 16:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0021_alter_bookinstance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('764529cc-3fae-4ab8-8218-ceab2f654404'), help_text='Уникальный ID для этого экземпляра книги из целой библиотеки', primary_key=True, serialize=False),
        ),
    ]
