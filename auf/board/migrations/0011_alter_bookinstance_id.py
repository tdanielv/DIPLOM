# Generated by Django 4.0.3 on 2022-03-10 16:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_alter_bookinstance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('22b536e8-c645-434c-8f08-e9431648e416'), help_text='Уникальный ID для этого экземпляра книги из целой библиотеки', primary_key=True, serialize=False),
        ),
    ]
