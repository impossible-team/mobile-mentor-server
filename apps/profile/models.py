from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    STATES = (
        (0, _('OFFLINE')),
        (1, _('ONLINE')),
        (2, _('READY TO PLAY')),
        (3, _('IN GAME'))
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    guid = models.UUIDField(blank=False, null=False, default=uuid4(), verbose_name=_('UUID'))
    state = models.IntegerField(blank=False, null=False, choices=STATES, default=0, verbose_name=_('State'))
    points = models.PositiveIntegerField(blank=False, null=False, default=0, verbose_name=_('Points'))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
