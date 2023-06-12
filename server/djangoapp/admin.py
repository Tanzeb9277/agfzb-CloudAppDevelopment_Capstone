from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2

# CarMakeAdmin class with CarModelInline


# CarModelAdmin class


# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)
