# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: caption,label
#     notebook_metadata_filter: latex_metadata
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.8.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   latex_metadata:
#     affiliation: TU Dresden
#     author: Debsankha Manik
#     title: Interplay Between Efficiency and Pooling
# ---

# # Introduction
# The most common ingredients of a scientific article are text (with equations typeset in $\LaTeX$) and figures. [Jupyter notebooks](https://jupyter.org/) are the tool of choice for many scientists for performing data analysis and producing figures for articles. However, jupyter notebooks allow the writer to put the text of an article and the computer code producing the figures in a single document. This leads to increased reproducibility, since the figures and the text being "out of sync" is reduced. A few elegant and easy to use workflows for creating documents using jupyter notebooks have aleady been presented. Here we will show one such workflow geared towards producing scientific articles meant to be submitted to journals. 
#
# ## The Goal
# We aim to achieve the following
#
# 1. All the ingredients of a scientific article is included in one or more jupyter notebooks. If lage datasets are needed, they can be accesses by the notebook from an external source. 
# 2. A single compilation step creates a $\LaTeX$ source and a compiled PDF for the article. 
# 3. The jupyter notebook should have the option to specify
#     * Equations in $\LaTeX$,
#     * Cross references,
#     * Bibliographies whose entries are maintained in one or more  `.bib` files, 
#     * And figure captions,
#     
#   which will be rendered corectly in the compiled PDF.
# 4. A `git` based workflow for collaboratively writing the article.
#
#
# ## The solution
# ### `git` support
# Jupyter notebooks don't work so well with git, so we will use [jupytext]
# [jupytext](https://jupytext.readthedocs.io/en/latest/install.html) to convert our notebooks into python scripts that work well with `git`. 
# ```bash
# # Convert the py files to ipynb
# jupytext --to ipynb --update-metadata '{"jupytext": {"notebook_metadata_filter":"latex_metadata", "cell_metadata_filter":"caption,label"}}'  hello.py
# # Convert the ipynb files to py files before checking in to git
# jupytext --to script --update-metadata '{"jupytext": {"notebook_metadata_filter":"latex_metadata", "cell_metadata_filter":"caption,label"}}'  hello.ipynb
# ```
#
#
#
# ### Converting the notebooks to $\LaTeX$
# The notebooks can be converted into LaTeX, and PDF using `nbconvert` and a supplied
# REVTeX template inspired by this blog post by [Julius
# Schulz](http://blog.juliusschulz.de/blog/ultimate-ipython-notebook).
# ```bash
# # Convert the ipynb to latex using nbconvert
# jupyter nbconvert --to=latex --template=revtex_nocode.tplx efficiency_price.ipynb
# # Compile the latex file into a PDF
# latexmk -pdf efficiency_price
# ```
#
# ### Cross references
# Just use `\label{bla}` \label{crossref} and `\ref{bla}` \ref{crossref} in any markdown cell as you would in a
# LaTeX document. The cross references won't be rendered properly in the jupyter
# notebook, but the LaTeX output will be just fine. Referencing equations such as 
#
# \begin{equation}
# E=mc^2 \label{eq-foo}
# \end{equation}
# is also possible. Here is a reference to the last equation \ref{eq-foo}. 
#
# ### Bibliography
# The generated LaTeX file will read the bibliography file `biblio.bib`. One can
# specify additional bibliography files or customize the generated bibliography arbitrarily by editing the following section in the `revtex_nocode.tplx` template
# ```tex
# ((* block bibliography *))
# \bibliographystyle{unsrt}
# \bibliography{biblio}
# ((* endblock bibliography *))
# ```
#
# To actually cite a bibliography entry with a key `newm` inside a markdown cell, one needs to add the following <cite data-cite="newm">(Newman)</cite>:
# ```html
# <cite data-cite="newm">(Newman)</cite>.
# ``` 
#
# ### Document title, author and affiliation
# We can add these as metadata to the jupyter notebook itself, which will then automatically be translated into appropriate $\LaTeX$ commands. On the menu bar, click on "Edit" -> "Edit Notebook Metadata". A window containing metadata in JSON will pop up. There one has to add/edit the following entries:
# ```json
#   "latex_metadata": {
#     "affiliation": "University of XXX",
#     "author": "John Doe",
#     "title": "A Study"
#   }
# ```
# **Note:** The text field so edited must be a valid JSON. That means, no trailing comma after the last entry.
#
# ### Figure captions, labels and referencing them
# Likewise we can add figure captions and optionally labels as cell metadata.
# On the menu bar, one needs to click on "View" -> "Cell Toolbar" -> "Edit Metadata". Now, in
# the menu bar of the code cell generating a plot, one needs to click on "Edit Metadata". Now the following JSON key/value pairs need to be added:
# ```json
# {
#   "caption": "A caption",
#   "label": "fig:bla"
# }
# ```

# +
# load libraries and set plot parameters
import numpy as np

import matplotlib.pyplot as plt
# %matplotlib inline

from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'png')
plt.rcParams['savefig.dpi'] = 75

plt.rcParams['figure.autolayout'] = False
plt.rcParams['figure.figsize'] = 10, 6
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2.0
plt.rcParams['lines.markersize'] = 8
plt.rcParams['legend.fontsize'] = 14

plt.rcParams['text.usetex'] = True
#plt.rcParams['font.family'] = "serif"
plt.rcParams['font.serif'] = "cm"
plt.rcParams['text.latex.preamble'] = r"\usepackage{subdepth,type1cm,amsmath,amssymb}"
# -

# #### A sample figure
# Here we have Figure \ref{fig:bla}, which we here reference.

# + caption="A caption" label="fig:bla"
x = np.linspace(-1,1,100)
fig, ax = plt.subplots()

ax.plot(x, np.tanh(x), label='tanh')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend();
# -


