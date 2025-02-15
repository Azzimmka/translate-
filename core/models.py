from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50),
    ) 

    class Meta:
        verbose_name = _('Котегория')
        verbose_name_plural = _('Котегории')

    def __str__(self):
        return self.name

class Post(TranslatableModel):
    category = models.ForeignKey(Category, related_name=_('category'), on_delete=models.SET_NULL, null=True, blank=True)
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=50),
        content = models.TextField(_('content'), default="Enter content...") ,
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')

    def __str__(self):
        return self.title

