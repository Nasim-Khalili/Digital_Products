from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self',verbose_name='parent',blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Name',max_length=50)
    description = models.TimeField(verbose_name='description',blank=True,null=True)
    avatar = models.ImageField(blank=True,upload_to='categories')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'categories'
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'


    def __str__(self):
        return self.title if self.title else "No Title"

class Product(models.Model):
    title = models.CharField(verbose_name='Name',max_length=50)
    description = models.TimeField(verbose_name='description',null=True, blank=True)
    avatar = models.ImageField(blank=True,upload_to='produvts')
    is_enable = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category',verbose_name='categories',blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'products'
    verbose_name = 'Product'
    verbose_name_plural = 'products'


class File(models.Model):
    product = models.ForeignKey('Product',verbose_name='product',on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Name',max_length=50)
    file = models.FileField('file',upload_to='file/%Y/%m/%d/')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'files'
    verbose_name = 'File'
    verbose_name_plural = 'files'