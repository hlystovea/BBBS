from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import file_size_validator, image_extension_validator


class Image(models.Model):
    image = models.ImageField(
        upload_to='images/',
        verbose_name=_('Изображение'),
        help_text=settings.IMAGE_FIELD_HELP_TEXT,
        validators=[file_size_validator, image_extension_validator],
    )
    image_caption = models.CharField(
        verbose_name=_('Подпись к изображению'),
        max_length=200,
    )

    class Meta:
        app_label = 'common'
        verbose_name = _('Изображение')
        verbose_name_plural = _('Изображения')

    def __str__(self):
        return f'{self.image_caption} ({self.image.width}x{self.image.height})'