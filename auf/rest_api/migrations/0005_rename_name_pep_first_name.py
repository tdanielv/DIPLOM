# Generated by Django 4.0.3 on 2022-03-10 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_pep_experience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pep',
            old_name='name',
            new_name='first_name',
        ),
    ]
