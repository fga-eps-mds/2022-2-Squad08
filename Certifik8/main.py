import argparse
import time
from .modules.generator.certificado import Certificados
from .modules.handler.tabela import Tabela
from .path import path_inicial
from .modules.utils import verificar_xlsx
from .modules.selection.file_selection import FileSelection
from .modules.selection.folder_selection import FolderSelection


def run():
    msg_help = 'Socorro!'
    parser =argparse.ArgumentParser(description=msg_help)
    if parser.parse_args() == parser.format_help():
        parser.print_help()
        exit()
    with open(
       file=path_inicial + "/constants/menu.txt",
        encoding="utf-8",
    ) as text:
        menu = text.read()

    print(menu)

    print()

    print("Selecione as tabela para gerar o certificado:")
    paths = FileSelection().run()

    for path in paths:
        print("\t" + path)

    print()

    time.sleep(3)

    print("Selecione a pasta para guardar os certificados:")

    path_destino = FolderSelection().run()
    print("\t" + path_destino)

    print()
    certificados = Certificados()
    tabela = Tabela()
    for path in paths:
        if verificar_xlsx(path):
            if tabela.set_data_frames(path):
                if tabela.verificar_tab_padrao(path_destino):
                    certificados.gerar_certificados(
                        path,
                        tabela.get_data_frame(),
                        tabela.get_data_frame_informacoes(),
                        path_destino,
                    )
        else:
            print(f"{path} - não é .xlsx, certificados não gerados!!!")

    return True
