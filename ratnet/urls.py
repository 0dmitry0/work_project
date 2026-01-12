from django.urls import path
from .views import LoginsList, LoginsAdd, LoginsEdit, LoginsDetail, LoginsDelete, LoginsChangeLog, LoginsBulkEditView, LoginsBulkDeleteView, InventoryList, InventoryDetail, InventoryAdd, StorageAdd, StorageList, StorageDetail, StorageEdit, InventoryDelete
from .models import DirtySecrets

app_name = "ratnet"

urlpatterns = [
    path("dirtysecrets/<int:pk>/edit", LoginsEdit.as_view(), name="dirtysecrets_edit"),
    path("dirtysecrets/<int:pk>/delete", LoginsDelete.as_view(), name="dirtysecrets_delete"),
    path("dirtysecrets/<int:pk>/changelog/", LoginsChangeLog.as_view(), name="dirtysecrets_changelog", kwargs={"model": DirtySecrets}),
    path("dirtysecrets/<int:pk>/", LoginsDetail.as_view(), name="dirtysecrets_detail"),
    path("dirtysecrets/add/", LoginsAdd.as_view(), name="dirtysecrets_add"),
    path('dirtysecrets/edit/', LoginsBulkEditView.as_view(), name='dirtysecrets_bulk_edit'),
    path('dirtysecrets/delete/', LoginsBulkDeleteView.as_view(), name='dirtysecrets_bulk_delete'),
    path("dirtysecrets/", LoginsList.as_view(), name="dirtysecrets_list"),
    path("dirtysecrets", LoginsList.as_view(), name="dirtysecrets"),

    path("inventory/<int:pk>/", InventoryDetail.as_view(), name="inventory_detail"),
    path("inventory", InventoryList.as_view(), name="inventory"),
    path("inventory/", InventoryList.as_view(), name="inventory_list"),
    path("inventory/add/", InventoryAdd.as_view(), name="inventory_add"),
    path('inventory/<int:pk>/edit', InventoryAdd.as_view(), name='inventory_edit'),
    path('inventory/<int:pk>/delete', InventoryDelete.as_view(), name='inventory_delete'),
    path('inventory/<int:pk>/changelog/', InventoryAdd.as_view(), name='inventory_changelog'),

    path('storage/<int:pk>/delete', StorageList.as_view(), name='storage_delete'),
    path('storage/<int:pk>/edit', StorageEdit.as_view(), name='storage_edit'),
    path('storage/<int:pk>/changelog/', StorageList.as_view(), name='storage_changelog'),
    path('storage/<int:pk>/', StorageDetail.as_view(), name='storage_detail'),
    path('storage/add', StorageAdd.as_view(), name='storage_add'),
    path('storage/edit', StorageAdd.as_view(), name='storage_bulk_edit'),
    path('storage/delete', StorageAdd.as_view(), name='storage_bulk_delete'),
    path('storage/', StorageList.as_view(), name='storage_list'),
    path('storage', StorageList.as_view(), name='storage')
]