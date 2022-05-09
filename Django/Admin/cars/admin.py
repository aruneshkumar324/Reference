from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    #fields = ['year', 'brand']

    fieldsets = [
        ('TIME INFORMATION', {'fields':['year']}),
        ('BRAND INFORMATION', {'fields': ['brand']})
    ]


admin.site.register(Car, CarAdmin)