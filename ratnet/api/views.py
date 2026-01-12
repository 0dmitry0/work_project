from netbox.api.viewsets import NetBoxModelViewSet
from ..models import DirtySecrets, Inventory, Storage
from .serializers import StorageSerializer

class StorageViewSet(NetBoxModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer