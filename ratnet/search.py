from netbox.search import SearchIndex, register_search
from .models import Inventory

@register_search
class GreenNetIndex(SearchIndex):
    model = Inventory
    fields = (
        ("inventory_name", 100),
    )
    display_attrs = ['login_name']
