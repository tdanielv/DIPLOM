# Generated by Django 4.0.3 on 2022-03-10 08:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_alter_bookinstance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3db72363-57be-423e-ad5f-1c6495e59682'), help_text='Уникальный ID для этого экземпляра книги из целой библиотеки', primary_key=True, serialize=False),
        ),
    ]