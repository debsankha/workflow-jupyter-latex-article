jupytext --to ipynb --update-metadata '{"jupytext": {"notebook_metadata_filter":"latex_metadata", "cell_metadata_filter":"caption,label"}}'  efficiency_price.py
jupyter nbconvert --to=latex --template=revtex_nocode.tplx efficiency_price.ipynb
pdflatex efficiency_price.tex
