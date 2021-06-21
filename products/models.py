from django.db import models
from user.models import MyUser
from django.utils.text import slugify
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Category(models.Model):
    slug_category = models.SlugField(unique=True)
    name_category = models.CharField(max_length=500, unique=True)
    image_category = models.ImageField(default="no-img.png", null=True, upload_to="category-pictures/")

    def save(self, *args, **kwargs):
        self.slug_category = slugify(self.name_category)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_category


class Products(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    slug_product = models.SlugField(max_length=500, unique=True, default="", null=True)
    name_product = models.CharField(max_length=500)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="Who_created")
    describe = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    main_picture = models.ImageField(default="no-img.png", null=True, upload_to="main-product-pictures/")
    category = models.ManyToManyField(Category, related_name="CategoryOfProduct")
    price = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    num_available = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug_product = slugify(self.name_product + "-" + str(now().timestamp()) + "-" + str(self.created_by.id))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_product


    def on_of_ratings(self):
        ratings = Rating.objects.filter(product=self)
        return len(ratings)

    def avg_ratings(self):
        sum=0
        ratings = Rating.objects.filter(product=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

class ProductPictures(models.Model):
    image_product = models.ImageField(upload_to="product-pictures/")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="PictureOfProduct")

# Linh
class Rating(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(5)])
    class Meta:
        unique_together = (('user', 'product'),)
        index_together = (('user', 'product'),)
