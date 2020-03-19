from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Complaint(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Yazar', on_delete=models.CASCADE, related_name='complaints')
    title = models.CharField(max_length=120, verbose_name='Başlık')
    text = models.TextField(verbose_name='Metin')
    created_date = models.DateTimeField(verbose_name='Yapıldığı Tarih', auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False, max_length=10)

    def __str__(self):
        return self.title

    