import os
import sys
sys.path.insert(0, os.path.abspath("."))

project = '{{ cookiecutter.package_name }}'
copyright = '{{ cookiecutter.copyright_year }}, {{ cookiecutter.author }}'
author = '{{ cookiecutter.author }}'
extensions = [
    "sphinx.ext.autodoc",
    "myst_parser"
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_static_path = ['_static']
myst_enable_extensions = [
    "colon_fence"
]
html_theme = "sphinx_book_theme"
html_sidebars = {
    "**": ["sbt-sidebar-nav.html", "sbt-sidebar-footer.html"]
}

