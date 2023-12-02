from django.db import models
from django.contrib.auth.models import User


from django.utils.translation import gettext as _, gettext_lazy
from django.utils.translation import pgettext_lazy
from django.core.cache import cache

class New(models.Model):
    title = models.CharField( verbose_name=gettext_lazy('Название'), max_length=50)
    text = models.TextField(verbose_name=gettext_lazy('Текст'))
    date = models.DateTimeField(verbose_name=gettext_lazy ('Время публикации'),auto_now_add=True)
    category = models.ForeignKey('Category', verbose_name=gettext_lazy('Категория'), on_delete=models.CASCADE)


    def preview(self):
        preview = f'{self.text[:128]}...'
        return preview


    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'



    class Meta:
        verbose_name = gettext_lazy ('Новость')
        verbose_name_plural = gettext_lazy ('Новости')

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, help_text=_('category title'))

    class Meta:
        verbose_name = gettext_lazy('Категория')
        verbose_name_plural = gettext_lazy ('Категории')

    def __str__(self):
        return f'{self.title}'


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )