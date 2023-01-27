import os
from ..modules.converter.html2pdf import Html2Pdf
from ..path import path_inicial


def test_converter_erro():
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    html2pdf = Html2Pdf(html=path_inicial + "/Melissa Ribeiro Araujo.html")
    assert not html2pdf.convert(
        output_name="Melissa Ribeiro Araujo.html",
        foldername="exemplo_Melissa",
        folder_destino=download_folder,
        output_funcao="MONITOR"
    )
