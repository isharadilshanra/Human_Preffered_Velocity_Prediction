from setuptools import find_packages
from setuptools import setup

setup(
    name='smrr_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('smrr_interfaces', 'smrr_interfaces.*')),
)
