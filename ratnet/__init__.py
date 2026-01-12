from netbox.plugins import PluginConfig

class GreenNetConfig(PluginConfig):
    name = 'GreenNet'
    verbose_name = 'GreenNet'
    description = 'GreenNet makes everything green like grass!'
    version = '1.0'
    author = 'Aponenko Dmitry'
    author_email = 'daponenk@gmail.com'
    base_url = 'greennet'

config = GreenNetConfig
