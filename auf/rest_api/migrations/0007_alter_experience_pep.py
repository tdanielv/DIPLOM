# Generated by Django 4.0.3 on 2022-03-10 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0006_rename_title_experience_pep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='pep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pep', to='rest_api.pep'),
        ),
    ]
