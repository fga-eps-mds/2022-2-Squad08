import os
from Certifik8.path import path_inicial
from ..modules.handler.tabela import Tabela


tabela = Tabela()


def test_set_data_frame_completa():
    """
    Verifica se o arquivo excel completo é lido corretamente.

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """

    assert tabela.set_data_frames(path_inicial + "/examples/completa.xlsx")


def test_set_data_frame_vazia():
    """
    Verifica se a exceção é lançada ao tentar ler uma tabela vazia.

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """

    assert not tabela.set_data_frames(path_inicial + "/examples/vazia.xlsx")


def test_set_data_frame_sem_coluna_informacoes():
    """
    Verifica se a exceção é lançada ao tentar ler uma tabela sem a coluna de
    informações.

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """

    assert not tabela.set_data_frames(
        path_inicial + "/examples/sem_coluna_informacoes.xlsx"
    )


def test_verificar_tabela_padrao():
    """
    Verifica se a tabela está no padrão esperado.

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """

    tabela.set_data_frames(path_inicial + "/examples/completa.xlsx")
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    assert tabela.verificar_tab_padrao(download_folder)


def test_verificar_set_data_frame_sem_col_info():
    """
    Verifica se a exceção é lançada ao tentar ler uma tabela sem a coluna de
    informações.

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """

    assert not tabela.set_data_frames(
        path_inicial + "/examples/sem_coluna_informacoes.xlsx"
    )


def test_verificar_set_data_frame_tabela_vazia():
    """
    Verifica se a exceção é lançada ao tentar ler uma tabela vazia.

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """

    assert not tabela.set_data_frames(path_inicial + "/examples/vazia.xlsx")
