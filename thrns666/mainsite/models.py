from django.db import models
from django.urls import reverse


# Create your models here.

class DataTable(models.Model):
    title = models.CharField(max_length=115, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    contacts = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to='photos/%y/')
    description = models.TextField(blank=True)


    def __str__(self):
        return self.title


class MainCategory(models.Model):
    name = models.CharField(max_length=50, db_index=True, null=True)

    def __str__(self):
        return self.name

class SubCategories(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    main_cat = models.ForeignKey('MainCategory', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    # def get_url(self):
    #     return reverse('product', kwargs={'product_id': self.pk})

class LastCategories(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Категории')
    sub_cat = models.ForeignKey('SubCategories', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id', 'name']


    def get_absolute_url(self):
        return reverse('catalog', kwargs={'category_id': self.pk})

class Product(models.Model):
    title = models.CharField(max_length=115, blank=True, verbose_name='Название')
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%y/')
    price = models.CharField(max_length=20, default='0', verbose_name='Стоимость')
    availability = models.BooleanField(default=True, verbose_name='Наличие')
    cat = models.ForeignKey('LastCategories', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'
        ordering = ['title', 'availability', 'price', 'cat']



    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})