from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Complaint(models.Model):
    user = models.ForeignKey('accounts.MyUser', verbose_name='Yazar', on_delete=models.CASCADE, related_name='complaints')
    title = models.CharField(max_length=120, verbose_name='Başlık')
    text = models.TextField(verbose_name='Metin')
    created_date = models.DateTimeField(verbose_name='Yapıldığı Tarih', auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False, max_length=10)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('complaint:detail', kwargs={'slug':self.slug})

    def get_create_url(self):
        return reverse('complaint:create')
    
    def get_delete_url(self):
        return reverse('complaint:delete', kwargs={'slug':self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        counter = 1
        while Complaint.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Complaint, self).save(*args, **kwargs)            
        