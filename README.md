# saao-pypackage-cookiecutter

Cookiecutter template for creating a Python package maintained by the South African Astronomical Observatory

## Prerequisites

Make sure [Cookiecutter](https://cookiecutter.readthedocs.io/) is installed on your computer.

```shell
cookiecutter --version
```

If it isn't installed, use any of the [available options to install it](https://cookiecutter.readthedocs.io/en/2.0.2/installation.html).

You should also make sure that all necessary versions of Python as well as tox are installed on your machine. [asdf](https://github.com/asdf-vm/asdf), [python-launcher](https://github.com/brettcannon/python-launcher) and [pipx](https://github.com/pypa/pipx/) may be of help in this regard.

For building the Python package you will also need the [build](https://github.com/pypa/build) tool.

The book *Publishing Python Packages* by Dane Hillard (Manning) provides good instructions for setting up all these various tools.

## Using the cookiecutter template

Use the cookiecutter template to create a new Python package project by running the following command.

```shell
cookiecutter https://github.com/saltastroops/saao-pypackage-cookiecutter.git
```

You will be prompted to provide various pieces of information. If you are happy with a suggested default value, you can just hit enter. The following table lists the details you are asked for.

Detail name | Description
--- | ---
author | Package author.
author_email | Email address of the package author.
copyright_year | Year to include in the license file.
lowest_supported_python_version | Lowest version of Python which can be used with the package. This must be given in a format understood by mypy (such as "py37" for Python 3.7). The version must be enclosed in double quotes. The value should be consistent with the value for `supported_python_versions`.
package_name | The name of the package, as used for PyPI. This will also be used as the name of the directory created for the project.
package_slug | The name of the package, as used in the code. A package (folder) with this name will be created in the `src` folder.
short_description | Short (one line) description of the package.
supported_python_versions | Comma separated list of the Python versions which can be used with the package. The versions must be given in a format understood by tox (such as "py37" for Python 3.7). Each version must be enclosed in double quotes.
url | URL of the package's repository.
version | Package version.

## After creating the project

After creating a project from this template, you should go to its root directory and create a virtual environment called `.venv`. (Technically, you could use any other name, but `.venv` is the name expected by python-launcher.)

```shell
python -m venv .venv
```

You should also consider putting the project under version control.

```shell
git init
```

Check all the project files, and the `setup.cfg` file in particular, and make any required changes.

## tox environments

The template defines several tox environments.

Environment | Executed command | Default arguments | Description
--- | --- | --- | ---
testenv | `pytest` | Run unit tests. |
format | `black` | Check for formatting issues | `--check --diff src test`
lint | `flake8` | Check for linting issues | `src test`
imports | `isort` | Check for incorrectly sorted import statements | `--check --diff src test`
typecheck | `mypy` | Check for type errors | `src test`
docs | `sphinx-build` | Check building the documentation | `-W -b html -d {envtmpdir}/doctrees docs {envtmpdir}/html`

If called without arguments, tox will run the testenv environment for all the python versions. To run it for a particular version, you can specify that version with the `-e` option. For example:

```shell
tox -e py38
```

Similarly, you can use the `-e` option for running any of the other environments.

```shell
tox -e format
tox -e lint
tox -e imports
tox -e typecheck
```

You can specify several options at the same time.

```shell
tox -e py37,py38
tox -e format,lint
```

Note that *there must be no comma between the environments*. You can also run tox for several environments at the same time by using the `-p` option.

```shell
tox -p -e p38,typecheck
```

This reduces the amount of execution time, but also the amount of output you get from tox.

## Documentation

The template creates a `docs` folder for the package documentation. This contains a [sphinx](https://www.sphinx-doc.org/en/master/) configuration file (`conf.py`) and an index file (`index.md`).

In order to add pages to the documentation, you need to add their Markdown or reStructured Text file to the treetoc directive in `index.md`. For example, if you have an additional API page in a file `api.md`, the treetoc directive might look as follows. Note that the index page with the toctree directive must not be included in the toctree directive.

    ```{toctree}
    ---
    hidden: true
    maxdepth: 2
    caption: Content
    ---

    api
    ```

The `hidden` property ensures that the content tree is not displayed on the index page. You still need the directive, though, so that sphinx knows how to populate the content tree in the sidebar.

Bu default, the [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/latest/) is used for the documentation. If you swap this for another theme, you should remove the theme package dependency (`sphinx-book-theme`) from the Sphinx configuration file (`docs/conf.py`), from the docs tox environment in `setup.cfg` and from the dev requirements file (`requirements-dev.txt`). You also have to remove or replace the `sidebar_html` configuration in the Sphinx configuration file, as required by the new theme.

## Development

For testing outside tox and for building the documentation you need various Python packages, which can be installed from the `requirements-dev.txt` file:

```shell
py -m pip install -r requirements-dev.txt
```

For unit tests run:

```shell
pytest
```

For formatting the code run:

```shell
black src test
```

For sorting import statements run:

```shell
isort src test
```

For linting run:

```shell
flake8 src test
```

For building the documentation run:

```shell
sphinx-build docs _build
```

## Acknowledgments

The template is largely based on Dane Hillard: *Publishing Python Packages* (Manning).
