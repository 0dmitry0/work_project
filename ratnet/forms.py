from netbox.forms import NetBoxModelForm, NetBoxModelBulkEditForm
from .models import DirtySecrets, Inventory, Storage
from . import encryption_dirty
from django import forms
from datetime import date
from utilities.forms.rendering import FieldSet
from django.utils.translation import gettext_lazy as _
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from django.contrib.auth.models import Group
from tenancy.models.contacts import ContactGroup
from dcim.models.devices import Device, Manufacturer
from utilities.forms.widgets import APISelectMultiple

class DirtySecretsBulkDeleteForm(NetBoxModelForm):
    model = DirtySecrets

class DirtySecretsBulkEditForm(NetBoxModelBulkEditForm):

    model = DirtySecrets

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        print(instance)
        groups = ContactGroup.objects.all()
        choices = [(cg.name, cg.name) for cg in groups]
        self.fields['login_work_group'].choices = choices

    login_name = forms.CharField(
        required=True, 
        label="login name",
        help_text="login here"
    )
    login_password = forms.CharField(
        required=True, 
        label="login password",
        help_text="password for this login",
        widget=forms.PasswordInput
    )
    login_master_password = forms.CharField(
        required=True, 
        label="login master password",
        help_text="Used to decrypt back password",
        widget=forms.PasswordInput
    )
    login_work_group = forms.MultipleChoiceField(
        required=True,
        label="work group",
        widget=forms.SelectMultiple(attrs={
            'class': 'form-select',
            'data-placeholder': 'it refets to netbox Contact Group'
        }),
    )

    login_comment = CommentField()

    field_order = [
        "login_name",
        "login_work_group",
        "login_password",
        "login_master_password"
    ]


    fieldsets = (
        FieldSet('login_name', 'login_password', 'login_work_group', name=_('Login creation')),
        FieldSet('login_master_password', name=_('Encryption with master-password')),
        FieldSet('login_comment', name=_('Comments section')),
    )


    class Meta:
        model = DirtySecrets
        fields = [
            "login_name",
            "login_work_group",
            "login_password",
            "login_master_password",
            "login_comment"
        ]

    def save(self, commit=True):
        obj = super().save(commit=False)
        login_master_password = self.cleaned_data.get("login_master_password")
        login_password = self.cleaned_data.get("login_password")
        obj.login_encrypted_password =  encryption_dirty.encrypt_password(login_master_password, login_password)
        obj.login_created_date = date.today()
        print(obj.login_encrypted_password)

        if commit:
            obj.save()
        
        return obj

class DirtySecretsForm(NetBoxModelForm):

    print(ContactGroup.objects.all())

    login_name = forms.CharField(
        required=True, 
        label="login name",
        help_text="login here"
    )
    login_password = forms.CharField(
        required=True, 
        label="login password",
        help_text="password for this login",
        widget=forms.PasswordInput
    )
    login_master_password = forms.CharField(
        required=True, 
        label="login master password",
        help_text="used for encryption and decryption",
        widget=forms.PasswordInput
    )

    login_work_group = DynamicModelChoiceField(
        queryset = ContactGroup.objects.all(),
        label="work group",
        required=False,
    )

    login_comment = CommentField()


    fieldsets = (
        FieldSet('login_name', 'login_password', 'login_work_group', name=_('Login creation')),
        FieldSet('login_master_password', name=_('Encryption with master-password')),
        FieldSet('login_comment', name=_('Comments section')),
    )

    class Meta:
        model = DirtySecrets
        fields = [
            "login_name",
            "login_work_group",
            "login_password",
            "login_master_password",
            "login_comment"
        ]

    def save(self, commit=True):
        obj = super().save(commit=False)
        login_master_password = self.cleaned_data.get("login_master_password")
        login_password = self.cleaned_data.get("login_password")
        obj.login_encrypted_password =  encryption_dirty.encrypt_password(login_master_password, login_password)
        obj.login_created_date = date.today()

        if commit:
            obj.save()
        
        return obj

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

#    inventory_number = forms.CharField(
#        required=False, 
#        label="inventory number",
#        help_text="inventory number or serial number"
#    )

    inventory_comment = CommentField()

    inventory_device_usage = DynamicModelChoiceField(
        queryset = Device.objects.all(),
        label="device attachment",
        required=False,
    )

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
