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

# Packages
import setuptools  # setup, find_packages, Command
import os
import sys
import json
import shutil

# Setup variables. Change as needed
NAME = "mapillary"  
VERSION = "1.0.7"
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
    "mercantile",
    "mapbox-vector-tile",
    "pytest",
    "vt2geojson",
    "shapely",
    "turfpy",
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


def locked_requirements(section):
    """Look through the 'Pipfile.lock' to fetch requirements by section."""
    with open("Pipfile.lock") as pip_file:
        pipfile_json = json.load(pip_file)

    if section not in pipfile_json:
        print("{0} section missing from Pipfile.lock".format(section))
        return []

    return [
        package + detail.get("version", "")
        for package, detail in pipfile_json[section].items()
    ]


class UploadCommand(setuptools.Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            shutil.rmtree(os.path.join(HERE, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system(f"{sys.executable} setup.py sdist bdist_wheel --universal")

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system(f"git tag v{VERSION}")
        os.system("git push --tags")

        sys.exit()


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
    install_requires=locked_requirements("default"),
    # # What Python version is required
    python_requires=REQUIRES_PYTHON,
    # # What package data to include
    include_package_data=True,
    # # List of classifiers for metadata on PyPI
    classifiers=CLASSIFIERS,
    # # What commands to run
    cmdclass={
        "upload": UploadCommand,
    },
    # # A dictionary mapping names of “extras” (optional features of your project) to strings or
    # # lists of strings specifying what other distributions must be installed to support those
    # # features
    # # Right now, this fetches development dependencies which are un-needed
    # extras_require={"dev": locked_requirements("develop")},
)
