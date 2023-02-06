import os
from bs4 import BeautifulSoup
from tqdm import tqdm
from ..converter.html2pdf import Html2Pdf
from ..utils import get_data, get_foldername
from ...path import path_inicial


class Certificados:
    def __init__(self):
        with open(
            file=path_inicial + "/constants/template.html",
            encoding="utf-8",
        ) as html:
            self.template = html.read()
        self.soup = None

    def substituir_span(self, class_name, content):
        try:
            self.soup.find("span", class_=class_name).replace_with(content)
            return True
        except Exception:
            return False

    def gerar_certificados(self, filepath, data_frame, data_frame_informacoes):
        for i in tqdm(
            data_frame.index,
            ncols=100,
            desc="Certifik8",
            colour="#ab47bd",
        ):
            try:
                self.soup = BeautifulSoup(self.template, "html.parser")

                dados_certificado = {
                    "nome_participante": data_frame["Nome"][i],
                    "cpf_participante": data_frame["CPF"][i],
                    "cargo_participante": data_frame["Função"][i],
                    "frequencia_participante": str(data_frame["Frequência"][i]),
                    "nome_evento": data_frame_informacoes.iloc[0, 0],
                    "carga_hor": data_frame_informacoes.iloc[1, 0],
                    "nome_prof": data_frame_informacoes.iloc[2, 0],
                    "nome_dep": data_frame_informacoes.iloc[3, 0],
                    "data_inicial": data_frame_informacoes.iloc[4, 0],
                    "data_final": data_frame_informacoes.iloc[5, 0],
                    "nome_decano": data_frame_informacoes.iloc[6, 0],
                    "data_emissao": get_data(),
                }

                for campo, dado in dados_certificado.items():
                    self.substituir_span(campo, dado)

                with open(
                    file=dados_certificado["nome_participante"] + ".html",
                    mode="w",
                    encoding="utf-8",
                ) as file:
                    file.writelines(self.soup.prettify())

                foldername = get_foldername(filepath)
                html2pdf = Html2Pdf(
                    html=dados_certificado["nome_participante"] + ".html"
                )
                html2pdf.convert(dados_certificado["nome_participante"], foldername)
            except KeyboardInterrupt:
                return False
            finally:
                os.remove(str(dados_certificado["nome_participante"]) + ".html")
        return True
