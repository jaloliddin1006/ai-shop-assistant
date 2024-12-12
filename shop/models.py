from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    icon = models.ImageField(upload_to='category/icons/', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')

    def __str__(self):
        return f"{self.name} <- {self.parent.name if self.parent else ''}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        db_table = 'categories'


class Tag(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Teg'
        verbose_name_plural = 'Teglar'
        db_table = 'tags'


class Brand(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='brand/logos/', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Brend'
        verbose_name_plural = 'Brendlar'
        db_table = 'brands'

class Color(BaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=7)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rang'
        verbose_name_plural = 'Ranglar'
        db_table = 'colors'

class Size(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'O\'lcham'
        verbose_name_plural = 'O\'lchamlar'
        db_table = 'sizes'


class Product(BaseModel):
    STATUS_CHOICES = (
        ('new', 'Yangi'),
        ('sale', 'Chegirma'),
        ('hot', 'Qiziqarli'),
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    description = RichTextField()
    body = RichTextField(null=True)
    tags = models.ManyToManyField(Tag, related_name='products')
    is_featured = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f"{self.name} - {self.category.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'
        db_table = 'products'


class ProductAttribute(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True, related_name='products')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rating = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Mahsulot xususiyati'
        verbose_name_plural = 'Mahsulot xususiyatlari'
        db_table = 'product_attributes'


class ProductImage(BaseModel):
    product = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product/images/')

    class Meta:
        verbose_name = 'Mahsulot rasmi'
        verbose_name_plural = 'Mahsulot rasmlari'
        db_table = 'product_images'

