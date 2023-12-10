from .models import New
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

from django.utils.translation import gettext as _, gettext_lazy


class NewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = _('вы не выбрали категорию')

    class Meta:
        model = New
        fields = ['title', 'text',  'category']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': gettext_lazy('Название публикации')}),
            'datе': DateTimeInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': gettext_lazy('Дата публикации')}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': gettext_lazy('Текст публикации')}),
            'category__title': TextInput(attrs={'class': 'form-control', 'placeholder': gettext_lazy('Категория')})
        }


def clean(self):
    cleaned_data = super().clean()
    text = cleaned_data.get("text")
    if text is not None and len(text) < 20:
        raise ValidationError({
            "text": gettext_lazy("Описание не может быть менее 20 символов.")
        })

    return text