QUARTO_FLAGS = --profile ipynb --to ipynb --no-clean $(QUARTO_META)
NOTEBOOKS = notebooks/02-machine-learning-fundamentals.ipynb notebooks/03-neural-networks.ipynb

.PHONY: all flatten

all: flatten

flatten: $(NOTEBOOKS)
	mv notebooks/quarto_src/*.ipynb notebooks/ 2>/dev/null || true
	rmdir notebooks/quarto_src 2>/dev/null || true

notebooks/02-machine-learning-fundamentals.ipynb: quarto_src/02-machine-learning-fundamentals.qmd
	quarto render $< $(QUARTO_FLAGS) --output-dir notebooks

notebooks/03-neural-networks.ipynb: quarto_src/03-neural-networks.qmd
	quarto render $< $(QUARTO_FLAGS) --output-dir notebooks
