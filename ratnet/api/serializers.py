from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import Inventory, Storage

class InventorySerializer(NetBoxModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'inventory_name',
            'inventory_type',
            'inventory_number',
            'inventory_comment',
            'inventory_status',
            'inventory_storage',
            'inventory_vendor',
        ]

class StorageSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:greennet-api:storage-detail'
    )

    class Meta:
        model = Storage
        fields = [
            'id',
            'url',
            'display',
            'storage_name',
            'storage_comment',
        ]
        brief_fields = [
            'id',
            'url',
            'display',
            'storage_name',
            'storage_comment',
        ]

    def get_display(self, obj):
        return str(obj)
