import os
from bs4 import BeautifulSoup
from ..modules.generator.certificado import Certificados
from ..modules.handler.tabela import Tabela
from ..path import path_inicial


certificado = Certificados()


def test_substituir_span():
    """
    Testa a substituição de uma tag span em um HTML.

    Verifica se a substituição foi realizada com sucesso

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """

    with open(
        file=path_inicial + "/constants/template.html",
        encoding="utf-8",
    ) as html:
        certificado.template = html.read()
    certificado.soup = BeautifulSoup(certificado.template, "html.parser")
    assert certificado.substituir_span("nome_participante", "Melissa Ribeiro")


def test_substituir_span_erro():
    """
    Testa a substituição de uma tag span em um HTML.

    Verifica se a substituição não foi realizada devido a um erro.

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """

    with open(
        file=path_inicial + "/examples/Melissa Ribeiro Araujo.html",
        encoding="utf-8",
    ) as html:
        certificado.template = html.read()
    certificado.soup = BeautifulSoup(certificado.template, "html.parser")
    assert not certificado.substituir_span("nome_participante", "Melissa Ribeiro")


def test_gerar_certificados():
    """
    Testa a geração de certificados a partir de uma tabela.

    Verifica se todos os certificados foram gerados corretamente.

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """

    tabela = Tabela()
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    tabela.set_data_frames(path_inicial + "/examples/tabela_1_reg.xlsx")
    assert certificado.gerar_certificados(
        path_inicial + "/examples/tabela_1_reg.xlsx",
        tabela.get_data_frame(),
        tabela.get_data_frame_informacoes(),
        download_folder,
    )
