import subprocess
from pepelatepeh import latex_doc, latex_image, latex_table


with open("image.tex", "w", encoding="utf-8") as f:
    f.write(latex_doc("code.png", latex_image))


with open("table.tex", "w", encoding="utf-8") as f:
    f.write(latex_doc([[1, 2], [3, 4]], latex_table))


subprocess.run(["pdflatex", "-interaction=nonstopmode", "image.tex"])
subprocess.run(["pdflatex", "-interaction=nonstopmode", "table.tex"])