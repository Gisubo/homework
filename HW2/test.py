import pepelatepeh as l


with open("image.tex", "w", encoding="utf-8") as f:
    f.write(l.latex_doc("code.png",l.latex_image))

with open("table.tex", "w", encoding="utf-8") as f:
    f.write(l.latex_doc([[1, 2], [3, 4]],l.latex_table))
