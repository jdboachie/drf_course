from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel,
)
from utils.model_abstracts import Model


class Contact(TimeStampedModel, ActivatorModel, TitleDescriptionModel, Model):
    class Meta:
        verbose_name_plural = "Contacts"

    email = models.EmailField(verbose_name="Email")

    def __str__(self) -> str:
        return f"{self.title}"
