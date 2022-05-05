from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Hotel(BaseModel):
    class Meta:
        verbose_name = _('Hotel')
        verbose_name_plural = _('Hotels')

    name = models.CharField(
        max_length=150,
        verbose_name=_('Name')
    )

    def __str__(self):
        return self.name


class Room(BaseModel):
    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        verbose_name=_('Hotel')
    )
