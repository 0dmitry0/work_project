import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from .models import Inventory, Storage
import django_tables2 as tables
from django.urls import reverse

class InventoryTable(NetBoxTable):

    inventory_name = tables.LinkColumn(
        "plugins:greennet:inventory_detail",
        args=[tables.A("pk")],
        verbose_name="inventory name"
    )

    class Meta(NetBoxTable.Meta):
        model = Inventory
        fields = (
            "inventory_name",
            "inventory_type",
            "inventory_status",
            "inventory_storage",
            "inventory_amount",
        )

class StorageTable(NetBoxTable):
    
    id = tables.LinkColumn(
        "plugins:greennet:storage_detail",
        args=[tables.A("pk")],
        verbose_name="ID"
    )

    class Meta(NetBoxTable.Meta):
        model = Storage
        fields = (
            "id",
            "storage_name",
            "storage_comment",
        )
