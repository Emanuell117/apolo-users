# -*- coding: utf-8 -*-
#
# apolo-docs documentation build configuration file, created by
# sphinx-quickstart on Wed Apr 18 15:48:51 2018.

import os
import sys

# -- General configuration ------------------------------------------------

extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'apolo-docs'
copyright = u'Creative Commons Attribution-NonCommercial 4.0 International License'
author = u'Centro de Computación Científica Apolo - Universidad EAFIT'

version = u'0.1'
release = u'0.1'

language = 'en'

exclude_patterns = []

pygments_style = 'sphinx'

todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': True,
    'style_nav_header_background': '#003d82',  # Color azul marino como en tu imagen
}

html_static_path = ['_static']

# SOLUCIÓN: Agregar estilos personalizados SIN sobrescribir los del tema
html_css_files = [
    'css/theme_overrides.css',
]

# El html_context ahora solo incluye contexto, no sobrescribe CSS
html_context = {
    'display_github': True,
    'github_user': 'Emanuell117',
    'github_repo': 'apolo-users',
}

html_logo = '_static/apolo-white.png'


# -- Options for HTMLHelp output ------------------------------------------

htmlhelp_basename = 'apolo-docsdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # 'papersize': 'letterpaper',
    # 'pointsize': '10pt',
    # 'preamble': '',
    # 'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'apolo-docs.tex', u'Apolo Scientific Computing Center's Documentation',
     u'The Apolo Team', 'manual'),
]


# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, 'apolo-docs', u'apolo-docs Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (master_doc, 'apolo-docs', u'apolo-docs Documentation',
     author, 'apolo-docs', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output ----------------------------------------------

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

epub_exclude_files = ['search.html']


# -- Options for the linkcheck builder ------------------------------------

linkcheck_ignore = [r'https://leto.eafit.edu.co']
