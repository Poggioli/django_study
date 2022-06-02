from django.contrib import admin

from mothies.models import Mothie


# Register your models here.
@admin.register(Mothie)
class MothieAdmin(admin.ModelAdmin):
    ...
