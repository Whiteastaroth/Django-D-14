from django_filters import FilterSet, ModelChoiceFilter, CharFilter, DateFilter
from django.forms import SelectDateWidget
from .models import Category
from django.utils.translation import gettext as _, gettext_lazy


class NewFilter(FilterSet):
    slug = ModelChoiceFilter(field_name= 'category__title',
                             queryset = Category.objects.all(),
                             label = gettext_lazy('Категория'),
                             empty_label = gettext_lazy('Любой')
                             )

    title = CharFilter(lookup_expr='contains',)

    date = DateFilter(field_name='data',
                      lookup_expr='gt',
                      label=gettext_lazy('Дата'),
                      widget=SelectDateWidget(attrs={'type': 'date'},)
                      )