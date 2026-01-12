from django.shortcuts import render
from django.shortcuts import redirect
from datetime import date
from . import encryption_dirty
from .models import DirtySecrets, Inventory, Storage
from .forms import DirtySecretsForm, DirtySecretsBulkEditForm, DirtySecretsBulkDeleteForm, InventoryForm, StorageForm
from netbox.views.generic import ObjectEditView, ObjectView, ObjectListView, ObjectDeleteView, ObjectChangeLogView, BulkEditView, BulkDeleteView
from .tables import DirtySecretsTable, InventoryTable, StorageTable
from ratnet.api.serializers import DirtySecretsSerializer, InventorySerializer, StorageSerializer
from . import encryption_dirty
from django.urls import reverse


class LoginsBulkEditView(BulkEditView):
    queryset = DirtySecrets.objects.all()
    form = DirtySecretsBulkEditForm
    model = DirtySecrets
    table = DirtySecretsTable

class LoginsBulkDeleteView(BulkDeleteView):
    queryset = DirtySecrets.objects.all()
    table = DirtySecretsTable

class LoginsList(ObjectListView):
    queryset = DirtySecrets.objects.all()
    table = DirtySecretsTable
    def post(self, request):
        if 'bulk_delete' in request.POST:
            selected_ids = request.POST.getlist('pk')
            print(selected_ids)
        return redirect(request.path)

class LoginsAdd(ObjectEditView):
    queryset = DirtySecrets.objects.all()
    form = DirtySecretsForm
    serializer_class = DirtySecretsSerializer

class LoginsEdit(ObjectEditView):
    model = DirtySecrets
    queryset = DirtySecrets.objects.all()
    form = DirtySecretsForm

class LoginsDetail(ObjectView):
    queryset = DirtySecrets.objects.all()
    template_name = "ratnet/dirtysecrets.html"

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = DirtySecrets.objects.get(pk=pk)
        master_password = request.POST.get('master_password')
        decrypted_password = encryption_dirty.decrypt_password(master_password, instance.login_encrypted_password)
        context = {
            "object": instance,
            "login_name": instance.login_name,
            "login_comment": instance.login_comment,
            "login_work_group": instance.login_work_group,
            "login_encrypted_password": decrypted_password,
        }
        return render(request, 'ratnet/dirtysecrets.html', context)

    def get_extra_context(self, request, instance):
        return {
            "login_name": instance.login_name,
            "login_comment": instance.login_comment,
            "login_work_group": instance.login_work_group,
            "login_encrypted_password": "None",
        }

class LoginsChangeLog(ObjectChangeLogView):
    pass

class LoginsDelete(ObjectDeleteView):
    queryset = DirtySecrets.objects.all()
    model = DirtySecrets


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