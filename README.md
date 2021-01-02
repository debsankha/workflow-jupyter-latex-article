# A workflow for collaborative reproducible scientific article writing
This repository consists of jupyter notebooks
converted to python scripts using
[jupytext](https://jupytext.readthedocs.io/en/latest/install.html).  The
notebooks can be converted into LaTeX, and PDF using `nbconvert` and a supplied
REVTeX template inspired by this blog post by [Julius
Schulz](http://blog.juliusschulz.de/blog/ultimate-ipython-notebook).

## Installing the dependencies
```bash
# Installing python packages
pip install -r requirements.txt
# Install and enable the `latex_envs` jupyter extension
jupyter nbextension install --py latex_envs --sys-prefix
jupyter nbextension enable latex_envs --sys-prefix --py
```

## Converting the py files into jupyter notebooks
```bash
# Convert the py files to ipynb, preserving important metadata
jupytext --to ipynb --update-metadata \
    '{"jupytext": {"notebook_metadata_filter":"latex_metadata,celltoolbar", "cell_metadata_filter":"caption,label"}}'\
    hello.py
```

## Converting the notebook into PDF
```bash
# Convert the ipynb to latex using nbconvert
jupyter nbconvert --to=latex --template=revtex_nocode.tplx hello.ipynb
# Compile the latex file into a PDF
latexmk -pdf hello
```

## Getting the LaTeX output look just *right*
### Cross references
Just use `\label{bla}` and `\ref{bla}` in any markdown cell as you would in a
LaTeX document. If you have the [latex_envs](https://rawgit.com/jfbercher/jupyter_latex_envs/master/src/latex_envs/static/doc/latex_env_doc.html)
notebook extension installed, as described above, the cross references will be rendered properly in the jupyter
notebook, as well as in the LaTeX output.

### Bibliography
The generated LaTeX file will read the bibliography file `biblio.bib`. You can
specify additional bibliography files or customize the generated bibliography arbitrarily by editing the following section in the `revtex_nocode.tplx` template
```tex
((* block bibliography *))
\bibliographystyle{unsrt}
\bibliography{biblio}
((* endblock bibliography *))
```

To actually cite a bibliography entry with a key `newm` inside a markdown cell, use `\cite{bla}`, as is ususal in $\LaTeX$.

### Document title, author and affiliation
On the menu bar, click on "Edit" -> "Edit Notebook Metadata". A window containing metadata in JSON will pop up. Add/edit the following entries:
```json
  "latex_metadata": {
    "affiliation": "University of XXX",
    "author": "John Doe",
    "title": "A Study"
  }
```
**Note:** The text field you will edit there must be a valid JSON. That means, no trailing comma after the last entry.

### Figure captions
On the menu bar, click on "View" -> "Cell Toolbar" -> "Edit Metadata". Now, in
the menu bar of the code cell generating a plot, click on "Edit Metadata". Now add the following JSON key/value pairs:
```json
{
  "caption": "A caption",
  "label": "fig:bla"
}
```

**Warnings**

* `nbconvert>=6` must **not** be used. That release introduces backward-incompatible changes in how custom templates
are to be passed. The official documentation did not work for me.
* `notebook>6.1.5` should **not** be used, if you want to use the `latex_envs`
  notebook extension, that renders cross references, citations and theorem
  environments nicely in the notebooks.
* By default, the contents of the code cells of the jupyter notebook will not
  show up in the LaTeX output, only the outputs of the cells. In a cell that
  outputs a matplotlib figure, care should be taken that no text output is additionaly
  produced. This is achieved by adding a training `;` after the last code line, e.g. `plt.plot(x,y);`.


**Relevant documentations**

* [Managing citations in the IPython Notebook](https://nbviewer.jupyter.org/github/jupyter/nbconvert-examples/blob/master/citations/Tutorial.ipynb).
* [nbconvert: Custom Templates](https://nbconvert.readthedocs.io/en/5.6.1/customizing.html#Custom-Templates).
* [Julius Schulz's blogpost on converting jupyter notebooks to LaTeX](http://blog.juliusschulz.de/blog/ultimate-ipython-notebook).
* [Latex_envs jupyter notebook extension](https://rawgit.com/jfbercher/jupyter_latex_envs/master/src/latex_envs/static/doc/latex_env_doc.html)
