from packaging import version
from django.conf import settings

NETBOX_CURRENT_VERSION = version.parse(settings.VERSION)

if NETBOX_CURRENT_VERSION >= version.parse("4.0.0"):
    from netbox.plugins import PluginMenuItem, PluginMenuButton
else:
    from extras.plugins import PluginMenuItem, PluginMenuButton

menu_items = (
        PluginMenuItem(
        link="plugins:greennet:inventory",
        link_text="GreenNet Inventory",
    ),
        PluginMenuItem(
        link="plugins:greennet:storage",
        link_text="GreenNet Storage",
    ),
)
