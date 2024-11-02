
import codecs
import os.path

from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")
    

setup(
    name="netbox-data-mover",
    version=get_version('netbox_data_mover/version.py'),
    description="A NetBox plugin to manage data movement configurations between various sources and destinations.",
    author="Eric Hester",
    author_email="hester1@clemson.edu",
    license="ApacheV2",
    url="https://github.com/erichester76/netbox-data-mover.git",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
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
    min_version="4.0.2",
    max_version="4.1.5"
)