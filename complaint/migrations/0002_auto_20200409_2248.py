# Generated by Django 3.0.3 on 2020-04-09 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='slug',
            field=models.SlugField(editable=False, max_length=100, unique=True),
        ),
    ]
