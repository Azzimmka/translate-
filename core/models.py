from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class Post(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=50),
        content = models.TextField(_('content'), default="No content") ,
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

