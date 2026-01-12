import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from .models import DirtySecrets, Inventory, Storage
import django_tables2 as tables
from django.urls import reverse

class DirtySecretsTable(NetBoxTable):

    id = tables.LinkColumn(
        "plugins:ratnet:dirtysecrets_detail",  # URL name of your detail view
        args=[tables.A("pk")],                 # Pass the object's PK
        verbose_name="ID"
    )

    pk = columns.ToggleColumn(
        visible=True,)

    login_name = tables.LinkColumn(
        "plugins:ratnet:dirtysecrets_detail",  # URL name of your detail view
        args=[tables.A("pk")],                 # Pass the object's PK
        verbose_name="login_name"
    )

    class Meta(NetBoxTable.Meta):
        model = DirtySecrets
        fields = (
            "login_name",
            "login_work_group",
            "login_created_date",
            "login_comment",
        )


class InventoryTable(NetBoxTable):

    inventory_name = tables.LinkColumn(
        "plugins:ratnet:inventory_detail",
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
        "plugins:ratnet:storage_detail",
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