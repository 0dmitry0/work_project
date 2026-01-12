from django.urls import path
from .views import InventoryList, InventoryDetail, InventoryAdd, StorageAdd, StorageList, StorageDetail, StorageEdit, InventoryDelete

app_name = "greennet"

urlpatterns = [
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
