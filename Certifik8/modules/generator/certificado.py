import os
from bs4 import BeautifulSoup
from tqdm import tqdm
from ..converter.html2pdf import Html2Pdf
from ..utils import get_data, get_foldername
from ...path import path_inicial


class Certificados:
    """
    Classe responsável por gerar certificados a partir de um template HTML
    e dados contidos em um data frame.

    Atributos:
        template (str): HTML que será utilizado como template para
        geração dos certificados.
        soup (bs4.BeautifulSoup): Objeto que representa o HTML com os
        dados de um participante.

    Métodos:
        substituir_span (str, str):
            Recebe o nome da classe e o conteúdo a ser inserido no HTML,
            substitui o primeiro span encontrado com classe igual a
            `class_name` pelo `content`.
        gerar_certificados (str, pandas.DataFrame, pandas.DataFrame, str):
            Recebe o caminho do arquivo CSV, data frames com dados
            dos participantes e informações do evento, além do
            caminho de destino dos arquivos PDF gerados, gerando os
            certificados e salvando-os no caminho especificado.
    """

    def __init__(self):
        with open(
            file=path_inicial + "/constants/template.html",
            encoding="utf-8",
        ) as html:
            self.template = html.read()
        self.soup = None

    def substituir_span(self, class_name, content):
        """
        Substitui o primeiro span encontrado com classe igual
        a `class_name` pelo `content`.

        Args:
            class_name (str): Nome da classe do span a ser substituído.
            content (str): Conteúdo a ser inserido no lugar do span.

        Returns:
            bool: True caso a substituição tenha sido bem sucedida,
            False caso contrário.
        """

        try:
            self.soup.find("span", class_=class_name).replace_with(content)
            return True
        except Exception:
            return False

    def gerar_certificados(
        self, filepath, data_frame, data_frame_informacoes, path_destino
    ):
        """
        Gera os certificados a partir do template HTML e dados
        contidos em um data frame.

        Args:
            filepath (str): Caminho do arquivo CSV com os dados
            dos participantes.
            data_frame (pandas.DataFrame): Data frame com os dados
            dos participantes.
            data_frame_informacoes (pandas.DataFrame): Data frame com
            as informações do evento.
            path_destino (str): Caminho de destino dos arquivos PDF gerados.

        Returns:
            bool: True caso a geração dos certificados tenha sido bem sucedida,
             False caso contrário
        """

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
                html2pdf.convert(
                    dados_certificado["nome_participante"],
                    foldername,
                    path_destino,
                    dados_certificado["cargo_participante"],
                )
            except KeyboardInterrupt:
                return False
            finally:
                os.remove(str(dados_certificado["nome_participante"]) + ".html")
        return True
