from django.contrib import admin
from .models import Organization, BusinessActivity, BusinessDivision, ProductCategory, ProductDesign

# Register your models here.
admin.site.register(Organization)
admin.site.register(BusinessActivity)
admin.site.register(BusinessDivision)
admin.site.register(ProductCategory)
admin.site.register(ProductDesign)
