import re
from Certifik8.modules.utils import get_foldername, verificar_xlsx, get_data
from Certifik8.path import path_inicial


def test_data_emissao():
    regex = (
        r"^(0[1-9]|[12]\d|3[01])\sde\s(Janeiro|Fevereiro|Março|Abril|Maio|Junho|" +
        r"Julho|Agosto|Setembro|Outubro|Novembro|Dezembro)\sde\s(20)\d{2}$"
    )
    assert re.match(regex, get_data())


def test_foldername():
    assert get_foldername("/home/Certifik8/examples/completa.xlsx") == "completa"


def test_utils_verificar_xlsx():
    assert verificar_xlsx(path_inicial + "/examples/vazia.xlsx")


def test_utils_verificar_xlsx_erro():
    assert not verificar_xlsx(path_inicial + "/examples/Melissa Ribeiro Araujo.html")
