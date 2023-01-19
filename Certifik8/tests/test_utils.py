from ..modules.utils import *
import re


def validar_data_emissao(data):
    regex = r"^(0[1-9]|[12]\d|3[01])\sde\s(Janeiro|Fevereiro|Março|Abril|Maio|Junho|Julho|Agosto|Setembro|Outubro|Novembro|Dezembro)\sde\s(20)\d{2}$"
    if re.match(regex, data):
        return True
    else:
        return False

def test_data_emissao():
    assert validar_data_emissao(get_data())

def test_foldername():
    assert get_foldername("/home/Certifik8/examples/completa.xlsx") == "completa"
