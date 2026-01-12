from netbox.api.viewsets import NetBoxModelViewSet
from ..models import Inventory, Storage
from .serializers import StorageSerializer

class StorageViewSet(NetBoxModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
