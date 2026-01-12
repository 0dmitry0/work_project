from packaging import version
from django.conf import settings

NETBOX_CURRENT_VERSION = version.parse(settings.VERSION)

if NETBOX_CURRENT_VERSION >= version.parse("4.0.0"):
    from netbox.plugins import PluginMenuItem, PluginMenuButton
else:
    from extras.plugins import PluginMenuItem, PluginMenuButton

menu_items = (
        PluginMenuItem(
        link="plugins:ratnet:dirtysecrets",
        link_text="Dirty secrets",
    ),
        PluginMenuItem(
        link="plugins:ratnet:inventory",
        link_text="Ratnet Inventory",
    ),
        PluginMenuItem(
        link="plugins:ratnet:storage",
        link_text="Ratnet Storage",
    ),
)