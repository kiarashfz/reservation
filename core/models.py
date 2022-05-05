from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False,
    )


class User(AbstractUser):
    pass
