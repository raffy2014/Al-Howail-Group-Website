from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(settings.STATIC_ROOT,'pattern')


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    profile = models.TextField()
    address = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField()
    faxno = models.CharField(max_length=100)
    telno = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        ordering = ["name"]

class BusinessActivity(models.Model):
    name = models.CharField(max_length=100)
    profile = models.TextField()
    address = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField()
    faxno = models.CharField(max_length=100)
    telno = models.CharField(max_length=100)   
    created_date = models.DateTimeField(default=timezone.now)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    division = models.ManyToManyField("BusinessDivision")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Business Sector"
        verbose_name_plural = "Business Sectors"
        ordering = ['name']


class BusinessDivision(models.Model):
    division = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField()
    faxno = models.CharField(max_length=100)
    telno = models.CharField(max_length=100)   
    created_date = models.DateTimeField(default=timezone.now)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    productcategory = models.ManyToManyField("ProductCategory")

    def __str__(self):
        return self.division

    class Meta:
        verbose_name = "Business Division"
        verbose_name_plural = "Business Divisions"
        ordering = ['division']

class ProductCategory(models.Model):
    category = models.CharField(max_length=100,unique=True)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
        ordering = ["category"]
    
class ProductDesign(models.Model):
    design = models.CharField(max_length=100,unique=True)
    photo = models.ImageField(upload_to="pattern",storage=fs)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)

    def __str__(self):
        return self.design
    
    class Meta:
        verbose_name = "Product Design"
        verbose_name_plural = "Product Designs"
        ordering = ["design"]

