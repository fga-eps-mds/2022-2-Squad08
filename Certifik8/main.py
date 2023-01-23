from tkinter import filedialog
from .modules.generator.certificado import Certificados
from .modules.handler.tabela import Tabela
from .path import path_inicial
from .modules.utils import verificar_xlsx


def run():
    with open(
        file=path_inicial + "/constants/menu.txt",
        encoding="utf-8",
    ) as text:
        menu = text.read()

    print(menu)

    paths = filedialog.askopenfilenames()

    for path in paths:
        print("\t" + path)

    print()

    certificados = Certificados()
    tabela = Tabela()
    for path in paths:
        if verificar_xlsx(path):
            if tabela.set_data_frames(path):
                if tabela.verificar_tab_padrao():
                    certificados.gerar_certificados(
                        path,
                        tabela.get_data_frame(),
                        tabela.get_data_frame_informacoes(),
                    )
        else:
            print(f"{path} - não é .xlsx, certificados não gerados!!!")

    return True
