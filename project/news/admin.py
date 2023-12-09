from django.contrib import admin
from .models import New, Category

from modeltranslation.admin import TranslationAdmin

class CategoryAdmin(TranslationAdmin):
    model = Category


class RecordlAdmin(TranslationAdmin):
    model = New

admin.site.register(New)
admin.site.register(Category)
# Register your models here.
