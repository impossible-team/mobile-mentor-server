from uuid import uuid4
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from topic.models import Block, Topic
from game.models import Game


class Profile(models.Model):
    STATE_OFFLINE = 0
    STATE_ONLINE = 1
    STATE_READY_TO_PLAY = 2
    STATE_IN_GAME = 3

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
    blocks = models.ManyToManyField(Block, verbose_name=_('Blocks'))

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return self.user.username

    def is_topic_studied(self, topic_id):
        topic_block_count = Block.objects.filter(topic=topic_id).count()
        topic_block_studied_count = self.blocks.filter(profile__blocks__topic=topic_id).count()
        return topic_block_count == topic_block_studied_count if topic_block_count > 0 and topic_block_studied_count > 0 else False

    def topic_studied_count(self):
        topic_studied = [bool(self.is_topic_studied(topic.pk)) for topic in Topic.objects.all()]
        return sum(topic_studied)

    def game_won(self):
        return Game.objects.filter(winner=self).count()

    def game_count(self):
        return Game.objects.filter(Q(player1=self) | Q(player2=self)).count()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
