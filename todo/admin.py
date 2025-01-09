from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.todo)
class TodoAdmin(admin.ModelAdmin):
    pass