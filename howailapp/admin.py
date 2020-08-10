from django.contrib import admin
from .models import BusinessType, BusinessTypeDivision, DivisionProductType, DivisionProductSizes, DivisionProductPattern, DivisionProductList

# Register your models here.
admin.site.register(BusinessType)
admin.site.register(BusinessTypeDivision)
admin.site.register(DivisionProductType)
admin.site.register(DivisionProductSizes)
admin.site.register(DivisionProductPattern)
admin.site.register(DivisionProductList)