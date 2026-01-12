from netbox.plugins import PluginConfig

class RatNetConfig(PluginConfig):
    name = 'ratnet'
    verbose_name = 'RatNet'
    description = 'Your RatNet plugin description'
    version = '1.0'
    author = 'Your Name'
    author_email = 'your.email@example.com'
    base_url = 'ratnet'

config = RatNetConfig