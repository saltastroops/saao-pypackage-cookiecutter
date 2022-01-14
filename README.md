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

By default, the [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/latest/) is used for the documentation. If you swap this for another theme, you should remove the theme package dependency (`sphinx-book-theme`) from the Sphinx configuration file (`docs/conf.py`), from the docs tox environment in `setup.cfg` and from the dev requirements file (`requirements-dev.txt`). You also have to remove or replace the `sidebar_html` configuration in the Sphinx configuration file, as required by the new theme.

### Docstrings

The template is adding [numpydoc](https://numpydoc.readthedocs.io/en/latest/) as a Sphinx extension. This implies that Python docstrings should be formatted according to the [numpydoc style guide](https://numpydoc.readthedocs.io/en/latest/format.html). You might also want to have a look at the [AstroPy style guide](https://docs.astropy.org/en/latest/development/style-guide.html#astropy-style-guide).

All numpydoc warnings for validation during a Sphinx build are enabled by default. If you want to be less restrictive, you may change the value of the `numpydoc_validation_checks` parameter in the `conf.py` file. For example, if you don't want to enforce types for parameters (but want to keep all other checks), you could use:

```shell
numpydoc_validation_checks = {"all", "PR04"}
```

As another example, if you only care about checking that there *are* docstrings and that their sections are in the correct order, you could use:

```shell
numpydoc_validation_checks = {"GL08", "GL07"}
```

See the [numpydoc validation page](https://numpydoc.readthedocs.io/en/latest/validation.html) for more details, including a list odf all the built-in validation checks.

Due to the way autodoc is handling code, you have to use reStructured Text in docstrings; MyST markdown will not work.

### Referencing code

Sphinx has the hierarchial concept of domains, roles and artifacts. For example, there is a `py` domain with a set of roles like `mod` or `class` (see below), which in turn contain a variety of artifacts. The combination of domain, role and artifact can be regarded as an address which can be referenced and linked to.

Assume we have a Python module `toolkit`. This would correspond to an artifact `toolkit` belonging to the `py` domain and the `mod` role. In reStructured text you would reference the module as follows:

```
:py:mod:`toolkit`
```

In MyST Markdown you would instead use:

```
{py:mod}`toolkit`
```

Similarlarly, if you have a class `Toolkit` in the `toolkit` module, you can reference it as follows in reStructured Text and MyST Markdown, respectively:

```
:py:class:`toolkit.Toolkit`
```

```
{py:class}`toolkit.Toolkit`
```

The `py` domain [has the following roles](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html).

---|---
Role | Description
:py:mode: | Module or package.
:py:func: | Function. Parentheses will be added automatically by Sphinx if the `add_function_parentheses` config value is True (the default).
:py:data: | Module-level variable.
:py:const: | "defined" constant. This may be a Python variable that is not intended to be changed.
:py:class: | Class.
:py:meth: | Method of an object. The role text can include the type name and the method name; if it occurs within the description of a type, the type name can be omitted.
:py:attr: | Data attribute or property of an object.
:py:exc: | Exception.
:py:obj: | Object of unspecified type. Useful e.g. as the [default_role](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-default_role).

If you are using autodoc for generating documentation for your code, you can use these roles for referencing your code out of the box.

You may use roles for referencing within docstrings. However, as mentioned above, you have to use reStructured text in docstrings; MyST Markdown references will not work.

### Referencing code in other projects

Thanks to [intersphinx](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html), which is enabled by this template, you can reference code in other projects in the same way as you in your own project. So for example, Python's `list` class can be referenced in reStructured text with

```
:py:class:`list`
```

and in MyST Markdown as

```
{py:class}`list`
```

However, you need to declare the other projects in the `conf.py` file. For example:

```
intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None),
    'matplotlib': ('http://matplotlib.org/', None),
    'astropy': ('http://docs.astropy.org/en/stable/', None)
}
```

If the same artifact name is used by different projects, you can resolve the ambiguity by qualifying the name with the project's key from the `intersphinx_mapping` dictionary. So for example, using the configuration above, the following reference in reStructured Text makes it explicit that you are referring to the `time` module in the Python documentation:

```
:py:mod:`python:time`
```

Similarly, in MyST you would use:

```
{py:mod}`python:time`
```

References to code in your project do not require a qualifier.

You may find out more about intersphinx from [Brian Skinn's PyOhio's 2019 presentation](https://youtu.be/CfInPYkbTZE).

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
