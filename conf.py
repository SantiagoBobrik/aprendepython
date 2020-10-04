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


# -- Project information -----------------------------------------------------

project = 'aprendepython'
# Description just for Latex purposes
description = 'Aprende Python'
copyright = '2020 <a href="https://sdelquin.me">Sergio Delgado Quintero</a>'
author = 'Sergio Delgado Quintero'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'es'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autosectionlabel_prefix_document = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

html_theme_options = {
    'logo': 'logo-aprendepython.png',
    'page_width': '1008px',
    'show_powered_by': True,
    'fixed_sidebar': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_show_sourcelink = False
html_show_sphinx = False

html_sidebars = {
    'index': ['about.html', 'searchbox.html', 'navigation.html'],
    '**': ['about.html', 'searchbox.html', 'innertoc.html'],
}

html_css_files = ['custom.css']
html_js_files = ['custom.js']

# -- Latex configuration ---------------------------------------------------

# xelatex engine & Symbola font allow using emojis (black&white thought)
# Symbola ttf: https://github.com/gearit/ttf-symbola/blob/master/Symbola.ttf

latex_engine = 'xelatex'

latex_elements = {
    'pointsize': '12pt',
    'fontpkg': r'''
\usepackage{fontspec}
\setmainfont{Symbola}
''',
}

latex_logo = '_static/logo-aprendepython.png'

latex_documents = [('index', 'main.tex', description, author, 'manual',)]
