
from setuptools import setup, find_packages

setup(
    name="netbox_data_mover",
    version="0.0.1",
    description="A NetBox plugin to manage data movement configurations between various sources and destinations.",
    author="Eric Hester",
    author_email="hester1@clemson.edu",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.1',
        'djangorestframework',
        'django-tables2',
        'django-filter',
        'pyvmomi',
        'dnacentersdk',
        'pysnmp',
        'prometheus-api-client',
        'pandas'
    ],
)
