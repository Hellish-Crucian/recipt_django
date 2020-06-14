from django.contrib import admin
from core import models


# Register your models here.


@admin.register(models.Recipt)
class ReciptAdmin(admin.ModelAdmin):
    list_display = ('title', 'Author')