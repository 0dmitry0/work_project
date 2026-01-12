from netbox.api.routers import NetBoxRouter
from .views import StorageViewSet

router = NetBoxRouter()
router.register('storage', StorageViewSet)
urlpatterns = router.urls