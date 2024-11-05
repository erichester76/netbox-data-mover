
from netbox.plugins import PluginConfig

class NetboxDataMoverConfig(PluginConfig):
    name = "netbox_data_mover"
    verbose_name = "NetBox Data Mover"
    description = "A NetBox plugin to manage data movement configurations between various sources and destinations."
    version = "4.1.0"
    author = "Eric Hester"
    author_email = "hester1@clemson.edu"
    base_url = "datamover"

config = NetboxDataMoverConfig
