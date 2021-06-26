# mapillary-python-sdk - Internal Resources

## Relevant Links

- Python naming conventions: https://pythonguides.com/python-naming-conventions/
- Building a Python Open Source Project: https://towardsdatascience.com/build-your-first-open-source-python-project-53471c9942a7
- Example geospatial Python library, which we can reference for inspiration: https://github.com/gboeing/osmnx
- Mapillary blog on API v4 examples: https://blog.mapillary.com/update/2021/06/23/getting-started-with-the-new-mapillary-api-v4.html


# mapillary-python-sdk -External Documentation

In this section, we keep a draft of the documentation.

<here we should give a paragraph describing the library and what its capabilities are>
  
## Getting Started
  
How do I install the Mapillary Python SDK? See the installation instructions <link to readthedocs.io>.

How do I use the Mapillary Python SDK? See the usage examples and tutorials in the examples repo <link to examples possibly>.

How does this function work? Check out the documentation.

### Basic Start

Making a virtual env,

```bash
python -m venv venv
source venv/bin/activate
```

To install the basic dependencies,

```bash
pip install -r requirements.txt
```

If you are going to work on the developer side,

```bash
pip install -r requirements_dev.txt
```

To deactivate the `virtualenv`,

```bash
deactivate
```

To run the formatter `black`, and the linter `flake8`, run,

```bash
flake8 mapillary & black mapillary
```
