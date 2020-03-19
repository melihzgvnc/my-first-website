# Generated by Django 3.0.3 on 2020-03-18 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Başlık')),
                ('text', models.TextField(verbose_name='Metin')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Yapıldığı Tarih')),
                ('slug', models.SlugField(editable=False, max_length=10, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
        ),
    ]