from ..modules.converter.html2pdf import Html2Pdf
from ..path import path_inicial


def test_converter_erro():
    html2pdf = Html2Pdf(html=path_inicial + "/Melissa Ribeiro Araujo.html")
    assert not html2pdf.convert(
        output_name="Melissa Ribeiro Araujo.html", foldername="exemplo_Melissa"
    )
