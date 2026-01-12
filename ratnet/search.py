from netbox.search import SearchIndex, register_search
from .models import DirtySecrets

@register_search
class DirtySecretsIndex(SearchIndex):
    model = DirtySecrets
    fields = (
        ("login_name", 100),
        ("login_work_group", 50),
        ("login_comment", 25),
    )
    display_attrs = ['login_name', 'login_work_group', 'login_comment']
