# mapillary-python-sdk - Internal Resources

## Relevant Links

- [Python naming conventions](https://pythonguides.com/python-naming-conventions/)
- [Building a Python Open Source Project](https://towardsdatascience.com/build-your-first-open-source-python-project-53471c9942a7)
- [Example geospatial Python library, which we can reference for inspiration](https://github.com/gboeing/osmnx)
- [Mapillary blog on API v4 examples](https://blog.mapillary.com/update/2021/06/23/getting-started-with-the-new-mapillary-api-v4.html)
- [Facebook Open Source Legal Terms](https://opensource.fb.com/legal/terms/)
- [Facebook Open Source Privacy Policy](https://opensource.fb.com/legal/privacy/)

## mapillary-python-sdk -External Documentation

In this section, we keep a draft of the documentation.

> here we should give a paragraph describing the library and what its capabilities are

## Getting Started
  
How do I install the Mapillary Python SDK? See the installation instructions ***link to readthedocs.io***.

How do I use the Mapillary Python SDK? See the usage examples and tutorials in the examples repo ***link to examples possibly***.

How does this function work? Check out the documentation.

### Basic Start

For installing `pipenv`, please see [here](https://pypi.org/project/pipenv/).

To install packages from `Pipfile`,

```bash
pipenv install
```

To install a package under `packages`,

```bash
pipenv install [package_name]
```

To install a package under `dev-packages`,

```bash
pipenv install --dev [package_name]
```

To run `python` with `pipenv`,

```bash
pipenv run python
```

To enter the virtual environment, run,

```bash
pipenv shell
```

### Formatting/Linting

To run the formatter `black`, and the linter `flake8`, run,

```bash
flake8 mapillary & black mapillary
```

Or, if you are on Linux, you can simply run,

```bash
make style
```

This runs the `style` policy from the `Makefile`.

### Building package

To build the package, run `python3 setup.py sdist bdist_wheel`. To test out a local installation, run `pip install -e .`.

## Contributing

We welcome contributions! See [CONTRIBUTING](CONTRIBUTING.md) for details on how to get started, and our [code of conduct](CODE_OF_CONDUCT.md).

## License

Mapillary-Python-SDK is MIT licensed, as found in the [LICENSE](LICENSE) file.
