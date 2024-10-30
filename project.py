import pyPDF2
import os

merger = pyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print (lista_arquivos)

for arquivos in lista_arquivos:
    if ".pdf" in arquivos:
        merger.append(f"arquivos/{arquivos}")


merger.write("PDF Final.pdf")

