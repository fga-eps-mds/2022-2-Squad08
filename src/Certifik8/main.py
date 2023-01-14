from src.Certifik8.certificado import Certificados
from tkinter import filedialog
import os


def run():
    certificados = Certificados()

    print(
        "Bem-vindo ao Certifik8, gerador de certificados da Semana Universitária da UnB"
    )

    paths = filedialog.askopenfilenames()

    for path in paths:
        if os.path.exists(path) and os.path.splitext(path)[1] == ".xlsx":
            certificados.gerarCertificados(
                path,
            )
        else:
            print("Tabela não encontrada")
