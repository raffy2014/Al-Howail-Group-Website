from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(settings.STATIC_ROOT,'pattern')


# Create your models here.
class BusinessType(models.Model):
    biztype = models.CharField(max_length=50)
    biztext = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.biztype
    
    class Meta:
        ordering = ['biztype']


class BusinessTypeDivision(models.Model):
    bizdivname = models.CharField(max_length=200)
    bizdivactivity = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    businesstype = models.ForeignKey(BusinessType, on_delete=models.CASCADE)

    def __str__(self):
        return self.bizdivname

    class Meta:
        ordering = ['bizdivname']

class DivisionProductType(models.Model):
    producttype = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    businesstypedivision = models.ForeignKey(BusinessTypeDivision, on_delete=models.CASCADE)

    def __str__(self):
        return self.producttype

    class Meta:
        ordering = ['producttype']

class DivisionProductSizes(models.Model):
    productsize = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    divisionproducttype = models.ForeignKey(DivisionProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.productsize

    class Meta:
        ordering = ['productsize']

class DivisionProductPattern(models.Model):
    sizepattern = models.CharField(max_length=200)
    photopattern = models.ImageField(upload_to="pattern",storage=fs)
    created_date = models.DateTimeField(default=timezone.now)
    divisionproducttype = models.ForeignKey(DivisionProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.sizepattern

    class Meta:
        ordering = ['sizepattern']

class DivisionProductList(models.Model):
    divisionproductsizes = models.ForeignKey(DivisionProductSizes, on_delete=models.CASCADE)
    divisionproductpattern = models.ForeignKey(DivisionProductPattern, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str('%s %s' % (self.divisionproductsizes, self.divisionproductpattern))

    class Meta:
        ordering = ['divisionproductsizes','divisionproductpattern']


