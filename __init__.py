
from extras.plugins import PluginConfig

class NetboxDataMoverConfig(PluginConfig):
    name = "netbox_data_mover"
    verbose_name = "NetBox Data Mover"
    description = "A NetBox plugin to manage data movement configurations between various sources and destinations."
    version = "0.1"
    author = "Eric Hester"
    author_email = "hester1@clemson.edu"
    base_url = "netbox_data_mover"

config = NetboxDataMoverConfig
