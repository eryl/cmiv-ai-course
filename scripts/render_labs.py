#!/usr/bin/env python
from pathlib import Path
import subprocess as sp
import click
from yaml import safe_load

@click.command()
@click.option("--quarto-config", default="_quarto-ipynb.yml", help="Path to quarto configuration file.")
@click.option("--output-path", default="labs", help="Path to output directory.")
@click.option("--notebook", default=None, help="Path to a single notebook to render (overrides quarto config).")
def main(quarto_config, output_path, notebook):
    print("Rendering notebooks...")
    data = safe_load(open(quarto_config, "r", encoding="utf-8"))
    if notebook is not None:
        notebooks = [notebook]
    else:
        notebooks = data.get("project", {}).get("render", [])
    output_path = Path(output_path)
    output_path.mkdir(exist_ok=True)
    for nb in notebooks:
        nb = Path(nb)
        out = output_path / nb.with_suffix(".ipynb")
        out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Converting {nb} -> {out}")
        sp.run(["quarto", "convert", nb, "-o", out], check=True)
        print(f"Postprocessing {out}")
        sp.run(["python", "./scripts/fix-ipynb.py", out], check=True)

if __name__ == "__main__":
    main()
