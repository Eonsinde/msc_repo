from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(NutritionTips)
class NutritionTipAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass