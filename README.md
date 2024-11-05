# NetBox Data Mover Plugin
## Summary

A NetBox plugin to manage data migration between various sources and destinations.

## Compatibility

| NetBox Version | Plugin Version |
|-------------|-----------|
| 4.x.x       | 4.1.1     |

## Installing

The plugin is available as a Python package in pypi and can be installed with pip  

```
sudo pip install netbox-data-mover
```
Enable the plugin in /opt/netbox/netbox/netbox/configuration.py:
```
PLUGINS = ['netbox_data_mover']
```
Enable Migrations:
```
cd /opt/netbox
sudo ./venv/bin/python3 netbox/manage.py makemigrations netbox_data_mover
sudo ./venv/bin/python3 netbox/manage.py migrate
```

Restart NetBox and add `netbox-data-mover` to your local_requirements.txt

See [NetBox Documentation](https://docs.netbox.dev/en/stable/plugins/#installing-plugins) for details
