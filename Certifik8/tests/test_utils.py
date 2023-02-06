import re
from Certifik8.modules.utils import get_foldername, verificar_xlsx, get_data
from Certifik8.path import path_inicial


def test_data_emissao():
    """
    Método de teste para a validação da data de emissão
    no formato dd de mês de aaaa, com dia representado
    por dois dígitos, mês por extenso e ano por quatro dígitos.

    Exemplos de entradas válidas:
        - 01 de Janeiro de 2020
        - 30 de Junho de 2022

    Retorna:
        assert re.match(regex, get_data())
        O método retorna o resultado da comparação da string
        retornada por get_data()com a expressão regular
        definida na variável "regex". Se a string corresponder
        ao padrão esperado, o método retorna None, indicando
        que a validação foi bem-sucedida.
    """

    regex = (
        r"^(0[1-9]|[12]\d|3[01])\sde\s("
        r"Janeiro|Fevereiro|Março|Abril|Maio|Junho|"
        + r"Julho|Agosto|Setembro|Outubro|Novembro|Dezembro)\sde\s(20)\d{2}$"
    )
    assert re.match(regex, get_data())


def test_foldername():
    """
    Testa a função `get_foldername` para garantir que o nome
    do diretório retornado está correto.

    Args:
        "/home/Certifik8/examples/completa.xlsx" (str):
            Caminho completo para o arquivo excel.
        "completa" (str): Nome esperado.

    Retorna:
        assert (bool): O método retorna o resultado da comparação.

    Example:
        >>> test_foldername("/home/Certifik8/examples/completa.xlsx")
        "completa"
    """

    assert get_foldername("/home/Certifik8/examples/completa.xlsx") == "completa"


def test_utils_verificar_xlsx():
    """
    Testa a função `verificar_xlsx` na verificação de
    um arquivo XLSX vazio.

    Args:
        path_inicial (str): Caminho inicial do projeto.

    Retorna:
        assert (bool): Retorna True se a função verificar
        corretamente o arquivo XLSX vazio.
    """

    assert verificar_xlsx(path_inicial + "/examples/vazia.xlsx")


def test_utils_verificar_xlsx_erro():
    """
    Testa a função verificar_xlsx quando é passado
    um arquivo com formato inválido.

    Esse teste verifica se a função verificar_xlsx
    retorna False quando é passado um arquivo
    com formato inválido, como um arquivo HTML neste caso.

    Retorna:
        bool: O resultado esperado é False,
        indicando que o arquivo passado
        não é um arquivo XLSX válido.
    """

    assert not verificar_xlsx(path_inicial + "/examples/Melissa Ribeiro Araujo.html")
