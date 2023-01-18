from html2pdf import Html2Pdf
import pandas as pd
import os
from Certifik8.constants.utils import get_data
from bs4 import BeautifulSoup

with open('../constants/template.html', encoding="utf-8") as html:
    html_doc = html.read()


class Certificados:

    def xlsx_content(self, path):
        data_frame = pd.read_excel(path)
        return data_frame

    def separarTabela(self, df):
        df_info = df[["Informações"]].copy()
        df_info = df_info.dropna(axis=0, how="all")
        df.drop(columns=["Informações"], inplace=True)
        return df_info

    def substituir_span(self, soup, class_name, content):
        soup.find("span", class_=class_name).replace_with(content)

    def gerarCertificados(
        self,
        filepath,
    ):
        try:
            df = self.xlsx_content(filepath)
            df.dropna(axis=0, how="all", inplace=True)
            # df.drop_duplicates(keep="first", inplace=True)
        except Exception as error:
            print(f'An error occurred: {error}')
            return

        df_info = self.separarTabela(df)

        data_emissao = get_data()
        for i in df.index:
            soup = BeautifulSoup(html_doc, "html.parser")
            self.substituir_span(soup, "nome_participante", df["Nome"][i])
            self.substituir_span(soup, "cpf_participante", df["CPF"][i])
            self.substituir_span(soup, "nome_evento", df_info.iloc[0, 0])
            self.substituir_span(soup, "carga_hor", df_info.iloc[1, 0])
            self.substituir_span(soup, "nome_prof", df_info.iloc[2, 0])
            self.substituir_span(soup, "nome_dep", df_info.iloc[3, 0])
            self.substituir_span(soup, "cargo_participante", df["Função"][i])
            frequencia = str(df["Frequência"][i])
            self.substituir_span(soup, "frequencia_participante", frequencia)
            self.substituir_span(soup, "data_inicial", df_info.iloc[4, 0])
            self.substituir_span(soup, "data_final", df_info.iloc[5, 0])
            self.substituir_span(soup, "nome_decano", df_info.iloc[6, 0])
            self.substituir_span(soup, "data_emissao", data_emissao)
            with open(df["Nome"][i] + ".html", "w") as file:
                file.writelines(soup.prettify())

            foldername = filepath.split("/")
            foldername = foldername[-1]
            foldername = foldername.split(".")[0]

            Html2Pdfs = Html2Pdf(html=df["Nome"][i] + ".html")
            Html2Pdfs.convert(df["Nome"][i], foldername)
            os.remove(df["Nome"][i] + ".html")
