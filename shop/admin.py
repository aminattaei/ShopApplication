from django.contrib import admin

from .models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "price", "created_time"]
    list_filter = ["price", "created_time"]
