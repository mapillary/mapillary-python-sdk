from setuptools import setup, find_packages, Command
import io, os, sys
from shutil import rmtree

name = "mapillary"
version = "0.0.1"
author = "Christopher Beddow, Omar Ali, Saif Ul Islam"
author_email = "cbed@fb.com, omarmuhammed1998.om@gmail.com, saifulislam84210@gmail.com"
description = "A Python 3 library built on the Mapillary API v4 to facilitate retrieving and working with Mapillary data"
long_description_content_type = "text/markdown"
url = "https://github.com/facebookexternal/mapillary-python-sdk"
requires_python = '>3.5'
here = os.path.abspath(os.path.dirname(__file__))
requirements = ["mercantile", "Fiona", "mapbox-vector-tile"]
classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',        
        "Programming Language :: Python :: 3.7",
    ]

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = description

# Load the package's __version__.py module as a dictionary
about = {}
if not version:
    project_slug = name.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = version

class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()

# Where the magic happens
setup(
    name=name,
    version=about['__version__'],
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url=url,
    packages=find_packages(),
    install_requires=requirements,
    python_requires=requires_python,
    include_package_data=True,
    classifiers=classifiers,
    cmdclass={
        'upload': UploadCommand,
    },    
)
