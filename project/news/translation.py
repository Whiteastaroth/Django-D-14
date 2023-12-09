from .models import Category, New
from modeltranslation.translator import register, TranslationOptions

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(New)
class NewTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)