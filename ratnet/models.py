from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from django.contrib.postgres.fields import ArrayField
from tenancy.models.contacts import ContactGroup

class Storage(NetBoxModel):

    storage_name = models.TextField(
        default=None,
        max_length=300
    )

    storage_comment = models.TextField(
        default=None,
        max_length=300
    )

    class Meta:
        ordering = ('storage_name',)

    def __str__(self):
        return f"{self.storage_name}"

    def get_absolute_url(self):
        return reverse("plugins:greennet:storage_detail", args=[self.pk])

    def get_edit_url(self):
        return reverse("plugins:greennet:storage_edit", args=[self.pk])


class Inventory(NetBoxModel):
    inventory_name = models.TextField(
        default=None,
        max_length=300
    )
    inventory_type = models.TextField(
        default=None,
        max_length=300,
        blank=True,
        null=True
    )
    inventory_comment = models.TextField(
        default=None,
        max_length=300,
        blank=True,
        null=True
    )
    inventory_status = models.CharField(
        default=None,
        max_length=300,
        blank=True,
        null=True
    )
    inventory_storage = models.ForeignKey(
        to='Storage',
        on_delete=models.PROTECT,
        related_name='storage_reference',
        blank=True,
        null=True,
    )
    inventory_vendor = models.ForeignKey(
        to='dcim.Manufacturer',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True,
        max_length=1,
    )
    inventory_amount = models.IntegerField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('inventory_name',)

    def __str__(self):
        return f"{self.inventory_name}"

    def get_absolute_url(self):
        return reverse("plugins:greennet:inventory_detail", args=[self.pk])

    def get_edit_url(self):
        return reverse("plugins:greennet:inventory_edit", args=[self.pk])
