from ..modules.handler.tabela import *


tabela = Tabela()

def test_set_data_frame_completa():
    assert tabela.set_data_frames('Certifik8/examples/completa.xlsx')

def test_set_data_frame_vazia():
    assert not tabela.set_data_frames('Certifik8/examples/vazia.xlsx')

def test_set_data_frame_sem_coluna_informacoes():
    assert not tabela.set_data_frames('Certifik8/examples/sem_coluna_informacoes.xlsx')