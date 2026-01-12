from django.shortcuts import render
from django.shortcuts import redirect
from datetime import date
from .models import Inventory, Storage
from .forms import InventoryForm, StorageForm
from netbox.views.generic import ObjectEditView, ObjectView, ObjectListView, ObjectDeleteView, ObjectChangeLogView, BulkEditView, BulkDeleteView
from .tables import InventoryTable, StorageTable
from ratnet.api.serializers import InventorySerializer, StorageSerializer
from django.urls import reverse

class InventoryDelete(ObjectDeleteView):
    queryset = Inventory.objects.all()
    model = Inventory    

class InventoryList(ObjectListView):
    queryset = Inventory.objects.all()
    table = InventoryTable

class InventoryAdd(ObjectEditView):
    queryset = Inventory.objects.all()
    form = InventoryForm

class StorageAdd(ObjectEditView):
    queryset = Storage.objects.all()
    form = StorageForm

class StorageList(ObjectListView):
    queryset = Storage.objects.all()
    table = StorageTable

class StorageEdit(ObjectEditView):
    queryset = Storage.objects.all()
    form = StorageForm  

class StorageDetail(ObjectView):
    queryset = Storage.objects.all()
    template_name = "ratnet/storage.html"
    def get_extra_context(self, request, instance):
        inventory = Inventory.objects.filter(inventory_storage=instance)
        number_value = inventory.count()
        return {
            "number_value": number_value,
            "inventory": inventory,
            "storage_name": instance.storage_name,
            "storage_comment": instance.storage_comment,
        }

class InventoryDetail(ObjectView):
    queryset = Inventory.objects.all()
    template_name = "ratnet/inventory.html"
    def get_extra_context(self, request, instance):
        return {
            "inventory_name": instance.inventory_name,
            "inventory_type": instance.inventory_type,
            "inventory_comment": instance.inventory_comment,
            "inventory_status": instance.inventory_status,
            "inventory_storage": instance.inventory_storage,
            "inventory_vendor": instance.inventory_vendor,
            "inventory_amount": instance.inventory_amount,
        }
