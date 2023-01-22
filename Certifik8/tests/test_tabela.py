from Certifik8.path import path_inicial
from ..modules.handler.tabela import Tabela


tabela = Tabela()


def test_set_data_frame_completa():
    assert tabela.set_data_frames(path_inicial + "/examples/completa.xlsx")


def test_set_data_frame_vazia():
    assert not tabela.set_data_frames(path_inicial + "/examples/vazia.xlsx")


def test_set_data_frame_sem_coluna_informacoes():
    assert not tabela.set_data_frames(
        path_inicial + "/examples/sem_coluna_informacoes.xlsx"
    )


def test_verificar_tabela_padrao():
    tabela.set_data_frames(path_inicial + "/examples/completa.xlsx")
    assert tabela.verificar_tab_padrao()


def test_verificar_set_data_frame_sem_col_info():
    assert not tabela.set_data_frames(
        path_inicial + "/examples/sem_coluna_informacoes.xlsx"
    )


def test_verificar_set_data_frame_tabela_vazia():
    assert not tabela.set_data_frames(path_inicial + "/examples/vazia.xlsx")
