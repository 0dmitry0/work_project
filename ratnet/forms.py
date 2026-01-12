from netbox.forms import NetBoxModelForm, NetBoxModelBulkEditForm
from .models import Inventory, Storage
from django import forms
from datetime import date
from utilities.forms.rendering import FieldSet
from django.utils.translation import gettext_lazy as _
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from django.contrib.auth.models import Group
from tenancy.models.contacts import ContactGroup
from dcim.models.devices import Device, Manufacturer
from utilities.forms.widgets import APISelectMultiple

class StorageForm(NetBoxModelForm):

    storage_name = forms.CharField(
        required=True,
        label="storage",
        help_text="add a storage to use it inside ratnet"
    )

    storage_comment = CommentField()

    fieldsets = (
        FieldSet('storage_name', 'storage_comment', name=_('Inventory storage creation')),
    )

    class Meta:
        model = Storage
        fields = [
            "storage_name", "storage_comment"
        ]
    def save(self, commit=True):
        obj = super().save(commit=False)

        if commit:
            obj.save()
        
        return obj

class InventoryForm(NetBoxModelForm):

    inventory_name = forms.CharField(
        required=True, 
        label="inventory name",
        help_text="inventory name, example: SFP+ module Test"
    )
    inventory_comment = CommentField()

    inventory_storage = DynamicModelChoiceField(
        queryset = Storage.objects.all(),
        label="where stored",
        help_text="specify storage if needed",
        required=False,
    )
    inventory_type = forms.ChoiceField(
        required=True,
        label="inventory type",
        choices=[('other','other'),('SFP','SFP'),('DAC','DAC')],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    inventory_status = forms.ChoiceField(
        required=True,
        label="inventory status",
        choices=[('available','available'),('in use','in use'),('reserved','reserved')],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    inventory_vendor = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        label="inventory vendor",
        help_text="select your vendor"
    )
    inventory_amount = forms.IntegerField(
        required=True,
        label="total amount of inventory",
        min_value=1,
        max_value=999999,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., 1001, 5000'
        }),
        help_text="total amount of inventory"
    )
    fieldsets = (
        FieldSet('inventory_name', 'inventory_type', 'inventory_status', 'inventory_amount', name=_('Inventory default fields')),
        FieldSet('inventory_vendor', name=_('Additional for SFP')),
        FieldSet('inventory_storage', name=_('Current location')),
        FieldSet('inventory_comment', name=_('Additional')),
    )

    class Meta:
        model = Inventory
        fields = [
            "inventory_name",
            "inventory_storage",
            "inventory_comment",
            "inventory_status",
            "inventory_amount",
            "inventory_type",
            "inventory_vendor",
        ]


    def save(self, commit=True):
        obj = super().save(commit=False)

        if commit:
            obj.save()
        
        return obj
