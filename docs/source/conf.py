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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


import glob
import os
import re
import sys

docs_src_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, docs_src_path)
src_path = os.path.abspath(os.path.join(docs_src_path, '..', '..'))
sys.path.insert(0, src_path)

import simple_parsing
import examples
# -- Project information -----------------------------------------------------

project = 'simple-parsing'
copyright = '2019, Fabrice Normandin'
author = 'Fabrice Normandin'

# The full version, including alpha/beta/rc tags
release = '0.0.3'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosummary',
    'numpydoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']



# -- Autodoc configuration -----------------------------------------------

autodoc_mock_imports = ['_version', 'utils._appdirs']

################################################################################
#                             Numpy Doc Extension                              #
################################################################################

# sphinx.ext.autosummary will automatically be loaded as well. So:
autosummary_generate = glob.glob("reference/*.rst")

# Generate ``plot::`` for ``Examples`` sections which contain matplotlib
numpydoc_use_plots = False

# Create a Sphinx table of contents for the lists of class methods and
# attributes. If a table of contents is made, Sphinx expects each entry to have
# a separate page.
numpydoc_class_members_toctree = False
