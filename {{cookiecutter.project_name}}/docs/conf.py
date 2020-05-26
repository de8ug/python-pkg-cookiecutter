# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# Add package to the path so it can be imported without installing it
sys.path.append(os.path.join(os.path.split(__file__)[0], os.pardir))
from {{ cookiecutter.package_name }} import __version__

# -- Project information -----------------------------------------------------

project = "{{ cookiecutter.project_name }}"
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.owner }}"
author = "{{ cookiecutter.owner }}"

# The full version, including alpha/beta/rc tags
release = __version__

# -- General configuration ---------------------------------------------------

master_doc = "index"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "{{ cookiecutter.html_theme.lower().replace('-', '_') }}"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "{{ cookiecutter.project_name }}.tex",
        "{{ cookiecutter.project_name }} Documentation",
        "{{ cookiecutter.owner }}",
        "manual",
    )
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "{{ cookiecutter.project_name }}",
        "{{ cookiecutter.project_name }} Documentation",
        [author],
        1,
    )
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "{{ cookiecutter.project_name }}",
        "{{ cookiecutter.project_name }} Documentation",
        author,
        "{{ cookiecutter.project_name }}",
        "{{ cookiecutter.project_short_description }}",
        "Miscellaneous",
    )
]
