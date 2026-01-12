from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import DirtySecrets, Inventory, Storage

class DirtySecretsSerializer(NetBoxModelSerializer):
    class Meta:
        model = DirtySecrets
        fields = [
            'id',
            'login_name',
            'login_created_date',
            'login_work_group',
            'login_comment',
            'login_encrypted_password',
        ]

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
        view_name='plugins-api:ratnet-api:storage-detail'
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

    def to_representation(self, instance):
        """Debug what's being sent in API response"""
        data = super().to_representation(instance)
        print(f"DEBUG Serializer output for {instance}: {data}")
        return data