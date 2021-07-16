from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class History(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    mentor = models.ForeignKey(
        User,
        verbose_name=_('Наставник'),
        on_delete=models.CASCADE,
    )
    child = models.CharField(
        verbose_name=_('Имя ребёнка'),
        max_length=100,
    )
    together_since = models.DateField(
        verbose_name=_('Вместе с'),
    )
    image = models.ImageField(
        verbose_name=_('Изображение'),
        upload_to='history/',
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name=_('Текст истории'),
    )
    output_to_main = models.BooleanField(
        verbose_name=_('Отображать на главной странице'),
        default=False,
    )
    raw_html = models.TextField(
        verbose_name=_('HTML'),
        max_length=4 * 10 ** 6
    )

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('История')
        verbose_name_plural = _('Истории')
        constraints = [
            models.UniqueConstraint(
                fields=['mentor', 'child'],
                name='mentor_and_child_uniq_together'),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.raw_html = ' '.join(self.raw_html.split())
        return super().save(*args, **kwargs)
