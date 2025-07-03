# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
setup.py

This file implements the configuration for uploading the projec to PyPi

Reference::
    1. https://packaging.python.org/tutorials/packaging-projects/
    2. https://www.youtube.com/watch?v=GIF3LaRqgXo

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

import os

import setuptools

# Setup variables. Change as needed
NAME = "mapillary"
VERSION = "1.0.14"
AUTHOR = "Christopher Beddow"
AUTHOR_EMAIL = "support@mapillary.zendesk.com"
LICENSE = "MIT"
PLATFORM = ["POSIX", "MacOS X", "Linux", "Windows"]
DESCRIPTION = (
    "A Python 3 library built on the Mapillary API v4 to facilitate retrieving and "
    "working with Mapillary data"
)
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"
URL = "https://github.com/mapillary/mapillary-python-sdk"
REQUIRES_PYTHON = ">=3.0"
HERE = os.path.abspath(os.path.dirname(__file__))
REQUIREMENTS = [
    "mapbox-vector-tile>=2.1.0",
    "mercantile>=1.2.1",
    "requests>=2.25.1",
    "vt2geojson>=0.2.1",
    "haversine>=2.3.1",
    "shapely>=2.1.0",
    "turfpy>=0.0.7",
    "geojson>=2.5.0",
]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Topic :: Scientific/Engineering :: GIS",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft",
    "Operating System :: MacOS",
    "Operating System :: POSIX",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
PROJECT_URLS = {
    "Download": "https://pypi.org/project/mapillary/#files",
    "Release Notes": "https://github.com/mapillary/mapillary-python-sdk/releases",
    "Bug Tracker": "https://github.com/mapillary/mapillary-python-sdk/issues",
    "Source": "https://github.com/mapillary/mapillary-python-sdk",
    "Twitter": "https://twitter.com/mapillary",
    "Developer Resources": "https://www.mapillary.com/developer",
    "Community Forum": "https://forum.mapillary.com/",
    "Blog": "https://blog.mapillary.com/",
    "Facebook": "https://www.facebook.com/mapillary/",
    "Website": "https://www.mapillary.com/",
}
PACKAGE_DIR = {"": "src"}

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
        LONG_DESCRIPTION = "\n" + f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

# Where the magic happens
setuptools.setup(
    # METADATA
    # # Package name
    name=NAME,
    # # Package versioning
    version=VERSION,
    # # Author name(s)
    author=AUTHOR,
    # # License
    license=LICENSE,
    # # Platform specification
    platforms=PLATFORM,
    # # Author email(s)
    author_email=AUTHOR_EMAIL,
    # # Short description about the package
    description=DESCRIPTION,
    # # Long descirption about the package
    long_description=LONG_DESCRIPTION,
    # # Content type of the long description
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    # # URL to the project on GitHub
    url=URL,
    # # Dictionary of useful project related URLs
    project_urls=PROJECT_URLS,
    # Codebase, Wheel, Egg Setup
    # Setuptools for finding other needed packages from Pipfile
    packages=setuptools.find_packages(where="src"),
    # # Specifiy the package directory
    package_dir=PACKAGE_DIR,
    # # A string or list of strings specifying what other distributions need to be installed
    # # when this one is
    install_requires=REQUIREMENTS,
    # # What Python version is required
    python_requires=REQUIRES_PYTHON,
    # # What package data to include
    include_package_data=True,
    # # List of classifiers for metadata on PyPI
    classifiers=CLASSIFIERS,
)
