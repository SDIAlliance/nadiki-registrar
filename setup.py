# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "nadiki_registrar"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Facility Registry API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Facility Registry API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['nadiki_registrar=nadiki_registrar.__main__:main']},
    long_description="""\
    API for registering and managing data center facilities
    """
)

