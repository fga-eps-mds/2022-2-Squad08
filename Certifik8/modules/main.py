from tkinter import filedialog
import os
from Certifik8.modules.certificado import Certificados


def run():
    with open('../constants/logo.txt', encoding="utf-8") as text:
        logo = text.read()
    print(logo)
    print(
        "Bem-vindo ao Certifik8, gerador de " +
        "certificados da Semana Universitária da UnB"
    )
    print("Escolha as tabelas:")

    certificados = Certificados()

    paths = filedialog.askopenfilenames()

    for path in paths:
        if os.path.exists(path) and os.path.splitext(path)[1] == ".xlsx":
            certificados.gerarCertificados(
                path,
            )
        else:
            print("Tabela não encontrada")
