from django.db import models
from django.utils.translation import ugettext_lazy as _


class Topic(models.Model):
    """
    Модель описания темы
    """
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name=_('Name'))
    about = models.TextField(blank=True, null=True, verbose_name=_('About'))

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')

    def __str__(self):
        return self.name or self.__class__.__name__


class Block(models.Model):
    """
    Модель описания раздела
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name=_('Topic'), related_name='blocks')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Name'))
    content = models.TextField(blank=True, null=True, verbose_name=_('Content'))
    short_content = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _('Block')
        verbose_name_plural = _('Blocks')

    def __str__(self):
        return self.name or self.__class__.__name__


class Test(models.Model):
    """
    Модель тестов для очередного блока
    """
    block = models.ForeignKey(Block, blank=True, verbose_name=_('Block'), related_name='tests')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Name'))
    content = models.TextField(null=True, blank=True, verbose_name=_('Content'))
    correct_answer_code = models.PositiveIntegerField(null=False, blank=False, default=0, verbose_name=_('Correct answer'))

    class Meta:
        verbose_name = _('Test')
        verbose_name_plural = _('Tests')

    def __str__(self):
        return self.name or self.__class__.__name__
