#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Variables ------------------------------------------------------------
# See: https://stackoverflow.com/a/36331678
doc_name = 'OTRS Developer Manual'
doc_description = 'This is the description of the documentation.'
doc_version = '7.0'
doc_yearstamp = '2018'
doc_vendor = 'OTRS AG'
doc_url = 'https://otrs.com'
doc_datestamp = '2018-10-04'
doc_license = 'GNU Free Documentation License'

rst_prolog = """
.. |doc-name| replace:: {0}
.. |doc-description| replace:: {1}
.. |doc-version| replace:: {2}
.. |doc-yearstamp| replace:: {3}
.. |doc-vendor| replace:: {4}
.. |doc-url| replace:: {5}
.. |doc-datestamp| replace:: {6}
.. |doc-license| replace:: {7}
""".format(
doc_name,
doc_description,
doc_version,
doc_yearstamp,
doc_vendor,
doc_url,
doc_datestamp,
doc_license
)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.5.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks'
]

extlinks = {
    'sysconfig': (
        'https://users.otrs.com/~bu/doc-config-reference/html/en/content/%s',
        ''
    )
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'OTRS Developer Manual'
copyright = '2018, OTRS AG'
author = 'OTRS AG'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '7.0'
# The full version, including alpha/beta/rc tags.
release = '7.0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# Options for localization
locale_dirs = ['locale/']
gettext_compact = True

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_logo = '../_static/images/otrs-logo.png'
html_theme_path = ['../_sphinx-themes']
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']
html_style = 'css/otrs.css'

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'doc-developer'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # TODO: this is a workaround to write a replacement of left-right arrow to the PDF
    'preamble': '''
\usepackage{newunicodechar}
\newunicodechar{↔}{–}
''',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'doc-developer.tex', 'OTRS Developer Manual',
     'OTRS AG', 'manual'),
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'doc-developer', 'OTRS Developer Manual',
     author, 'doc-developer', 'Developer manual for OTRS.',
     'Miscellaneous'),
]

# -- Options for EPUB output ----------------------------------------------

# Supress "unknown mimetype for ..." warnings
suppress_warnings = ['epub.unknown_project_files']
