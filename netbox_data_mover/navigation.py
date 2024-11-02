
from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_data_mover:datamover_list',
        link_text='Data Mover Jobs',
        buttons=()
    ),
    PluginMenuItem(
        link='plugins:netbox_data_mover:datamoverdatasource_list',
        link_text='Data Sources',
        buttons=()
    ),
)