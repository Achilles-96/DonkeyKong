from setuptools import setup, find_packages
from distutils.command.install import INSTALL_SCHEMES

setup(
    name='Donkey Kong Game',
    version='0.1',
    description='A description.',
    include_package_data = True,
    packages=['.']
)
