
from netbox.plugins import PluginMenuItem, PluginMenuButton

menu_items = (
     PluginMenuItem(
        link="plugins:netbox_data_mover:datamover_list",
        link_text="Jobs",
        buttons=[
            PluginMenuButton(
                link="plugins:netbox_data_mover:datamover_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
            ),
            # PluginMenuButton(
            #     link="plugins:netbox_data_mover:datamover_bulk_import",
            #     title="Import",
            #     icon_class="mdi mdi-upload",
            # ),
        ]
    ),
    PluginMenuItem(
        link="plugins:netbox_data_mover:datamoverdatasource_list",
        link_text="Data Sources",
        buttons=[
            PluginMenuButton(
                link="plugins:netbox_data_mover:datamoverdatasource_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
            ),
            # PluginMenuButton(
            #     link="plugins:netbox_data_mover:datamoverdatasource_bulk_import",
            #     title="Import",
            #     icon_class="mdi mdi-upload",
            # ),
        ]
    ),
)