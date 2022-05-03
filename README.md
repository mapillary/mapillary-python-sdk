# Mapillary Python SDK

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />

[![LinkedIn][linkedin-shield]][linkedin-url]
[![Email][email-shield]][email-url]
[![Twitter][twitter-shield]][twitter-url]
[![Facebook][facebook-shield]][facebook-url]

[![](./assets/img/logo/PNG/MapillaryPythonSDK-Logo.png)](https://github.com/mapillary/mapillary-python-sdk/)

<!-- PROJECT LOGO -->
<div>
<p align="center">
    Mapillary's official Python SDK for GeoSpatial Data
    <br />
    <a href="https://mapillary.github.io/mapillary-python-sdk/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://colab.research.google.com/drive/1BPWMP5k7QhXFB6nlWckHC1r54vIR0v2L?usp=sharing">View Demo</a>
    ·
    <a href="https://github.com/mapillary/mapillary-python-sdk/issues/new?assignees=&labels=bug&template=bug_report.md&title=Bug+Report">Report Bug</a>
    ·
    <a href="https://github.com/mapillary/mapillary-python-sdk/issues/new?assignees=&labels=feature&template=feature_request.md&title=Feature">Request Feature</a>
    ·
    <a href="https://mapillary.github.io/mapillary-python-sdk/">See Documentation</a>
</p>
</div>

<!-- TABLE OF CONTENTS -->
## Table Of Contents

- [Mapillary Python SDK](#mapillary-python-sdk)
  - [Table Of Contents](#table-of-contents)
  - [About](#about)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Development](#development)
      - [Formatting/Linting](#formattinglinting)
      - [Dev Setup](#dev-setup)
      - [Trouble shooting](#trouble-shooting)
      - [Upgrading A Package](#upgrading-a-package)
    - [Possible Issues](#possible-issues)
  - [Contributing](#contributing)
  - [Acknowledgements](#acknowledgements)
  - [Links](#links)
  - [More About Mapillary](#more-about-mapillary)
  - [Legal](#legal)

## About

Mapillary's Python SDK provides an easy mechanism for accessing and retrieving information from Mapillary's web application.

For more information, please visit [Mapillary](https://www.mapillary.com) and [Mapillary's Blog](https://blog.mapillary.com).

## Getting Started

### Installation

To get started, simply install `mapillary` by running,

```bash
pip install mapillary
```

A quick demo,

```python
"""
Getting image coordinates from a nearby set of coordinates
"""

# Importing mapillary
import mapillary.interface as mly

# JSON import
import json

# Get image points close to in the given coordinates
data = mly.get_image_close_to(longitude=31, latitude=30).to_dict()

# Save the data as JSON
file_name = "get_image_close_to_1.json"
with open(file_name, mode="w") as f:
    json.dump(data, f, indent=4)
```

You can check out all the implemented functionality from the [demo](https://colab.research.google.com/drive/1BPWMP5k7QhXFB6nlWckHC1r54vIR0v2L?usp=sharing).

Or you can check out the [documentation](https://mapillary.github.io/mapillary-python-sdk/)!

### Development

#### Formatting/Linting

To run the formatter `black`, and the linter `flake8`, run,

```bash
flake8 mapillary & black mapillary
```

Or, if you are on Linux, you can simply run,

```bash
make style
```

This runs the `style` policy from the `Makefile`.

#### Dev Setup

Aliases for setting up the environment have been provided in `Makefile` to reduce burden of replication.

The steps to execute are, in order of running them,

1. `make setup-dev`: Install developer dependencies
2. `make build`: Build the package
3. `make local-install`: Install package locally in the dev environment

To use the new package installed locally, first use `pipenv` to change into the environment that the package was installed into by running,

```bash
pipenv shell
```

Then run,

```bash
python # assuming running python opens the Python3 shell
```

Then import and use as required,

```python
# import package here
import mapillary.interface as mly

# more code to follow here
```

#### Trouble shooting

If you get messed up dependencies, feel free to delete the `Pipfile.lock` file with `rm Pipfile.lock`, then start again with the first step in [Dev Setup](#dev-setup).

If you ever need to start with a clean build, you can always run `make clean` which will clean the `dist` directory, then you can simply start again from the second step in [Dev Setup](#dev-setup).

#### Upgrading A Package

If you upgrade any package in `Pipfile`, be sure to run `pipenv install` to update the `Pipfile.lock` as well.

### Possible Issues

<details>
<summary><b>Failed installation/dev setup because of <i>libgeos_c.so</i> or <i>libgeos_c_1.so</i></b></summary>
<br>
With UNIX based systems, you would to install the `geos` package with you package manager.

In debian systems, `sudo apt install geos`.
In arch based systems, `sudo pacman -S geos`.
</details>

## Contributing

We welcome contributions! See [CONTRIBUTING](CONTRIBUTING.md) for details on how to get started, and
our [code of conduct](CODE_OF_CONDUCT.md).

## Acknowledgements

- [Christopher Beddow](https://github.com/cbeddow) - for leading the project
- [Saif Ul Islam](https://github.com/rubix982)  - for developing the SDK under MLH fellowship
- [Omar Ali](https://github.com/OmarMuhammedAli) - for developing the SDK under MLH fellowship

## Links

## More About Mapillary

- [Website](https://www.mapillary.com)
- [Blog](https://blog.mapillary.com)
- [A blog showcasing the SDK](https://blog.mapillary.com/update/2021/12/03/mapillary-python-sdk.html)
- [Web App](https://www.mapillary.com/app)
- [Forum](https://forum.mapillary.com)
- [API V4 - Mapillary Blog](https://blog.mapillary.com/update/2021/06/23/getting-started-with-the-new-mapillary-api-v4.html)

## Legal

- [Facebook Open Source Legal Terms](https://opensource.fb.com/legal/terms/)
- [Facebook Open Source Privacy Policy](https://opensource.fb.com/legal/privacy/)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- Shields -->

[contributors-shield]: https://img.shields.io/github/contributors/mapillary/mapillary-python-sdk.svg?style=for-the-badge

[forks-shield]: https://img.shields.io/github/forks/mapillary/mapillary-python-sdk.svg?style=for-the-badge

[stars-shield]: https://img.shields.io/github/stars/mapillary/mapillary-python-sdk.svg?style=for-the-badge

[issues-shield]: https://img.shields.io/github/issues/mapillary/mapillary-python-sdk.svg?style=for-the-badge

[license-shield]: https://img.shields.io/github/license/mapillary/mapillary-python-sdk.svg?style=for-the-badge

[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0A66C2.svg?style=for-the-badge&logo=linkedin&logoColor=white

[email-shield]: https://img.shields.io/badge/gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white

[twitter-shield]: https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white

[facebook-shield]: https://img.shields.io/badge/facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white

<!-- URLs -->

[contributors-url]: https://github.com/mapillary/mapillary-python-sdk/graphs/contributors

[forks-url]: https://github.com/mapillary/mapillary-python-sdk/network/members

[stars-url]: https://github.com/mapillary/mapillary-python-sdk/stargazers

[issues-url]: https://github.com/mapillary/mapillary-python-sdk/issues

[license-url]: https://github.com/mapillary/mapillary-python-sdk/blob/master/LICENSE.txt

[linkedin-url]: https://www.linkedin.com/company/mapillary/

[email-url]: mailto:support@mapillary.zendesk.com

[twitter-url]: https://twitter.com/mapillary

[facebook-url]: https://www.facebook.com/mapillary/

[website-url]: https://www.mapillary.com

[blogs-url]: https://blog.mapillary.com

[application-url]: https://www.mapillary.com/app

[forum-url]: https://forum.mapillary.com
