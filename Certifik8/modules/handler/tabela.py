import os
import sys
import pandas as pd
from ..utils import get_foldername


class Tabela:
    """
    Classe utilizada para manipular tabelas em formato .xlsx.

    Atributos:
        data_frame : pandas.DataFrame
            Armazena a tabela completa
        data_frame_informacoes : pandas.DataFrame
            Armazena a tabela com as informações do evento
        data_frame_funcao : pandas.DataFrame
            Armazena a tabela com as funções dos participantes
        path : str
            Caminho da tabela de origem
        path_destino : str
            Caminho da pasta destino para salvar os certificados
        foldername : str
            Nome da pasta que será criada

    Métodos:
        gerar_pasta_subpastas_cert()
            Cria a pasta e subpastas para armazenar os certificados
        set_data_frames(filepath: str) -> bool
            Carrega a tabela em um objeto pandas.DataFrame
        separar_tabela(data_frame: pandas.DataFrame)
            Separa a tabela em informações do evento e
            funções dos participantes
        get_data_frame() -> pandas.DataFrame
            Retorna a tabela completa
        get_data_frame_informacoes() -> pandas.DataFrame
            Retorna a tabela com as informações do evento
        verificar_tab_padrao(folder_destino: str) -> bool
            Verifica se a tabela é padrão e cria a pasta e
            subpastas para armazenar os certificados
    """

    def __init__(self):
        """
        Construtor da classe Tabela. Inicializa os atributos
        com valores padrão:
            data_frame: None
            data_frame_informacoes: None
            data_frame_funcao: None
            path: None
            path_destino: None
            foldername: None
        """

        self.data_frame = None
        self.data_frame_informacoes = None
        self.data_frame_funcao = None
        self.path = None
        self.path_destino = None
        self.foldername = None

    def gerar_pasta_subpastas_cert(self):
        """
        Cria a pasta e subpastas para armazenar os certificados

            - Cria uma pasta principal com o nome especificado
            em 'self.foldername'
                no caminho de destino 'self.path_destino'.
            - Cria as subpastas com o nome das funções obtido do DataFrame
            'self.data_frame_funcao'.
            - Se a pasta de destino já existe, ela não será recriada.
            - Em caso de erro de permissão, a execução é interrompida
            com uma mensagem de erro.
        """

        try:
            if not os.path.exists(self.path_destino + "/" + self.foldername):
                os.makedirs(self.path_destino + "/" + self.foldername)
            for i in self.data_frame_funcao.index.tolist():
                if not os.path.exists(
                    self.path_destino
                    + "/"
                    + self.foldername
                    + "/"
                    + self.data_frame_funcao["Função"][i]
                ):
                    os.makedirs(
                        self.path_destino
                        + "/"
                        + self.foldername
                        + "/"
                        + self.data_frame_funcao["Função"][i]
                    )
        except PermissionError:
            print(
                "Pasta para receber os certificados não escolhida, "
                "certificados não gerados!!!"
            )
            sys.exit()

    def set_data_frames(self, filepath):
        """
        Carrega a tabela em um objeto pandas.DataFrame

        Parameters:
            file_path (str): Caminho do arquivo excel.

        Returns:
            bool: Retorna True em caso de sucesso ou False em caso de erro.
        """

        self.path = filepath
        self.foldername = get_foldername(self.path)
        try:
            self.data_frame = pd.read_excel(self.path)

            self.separar_tabela(self.data_frame)

            self.data_frame.dropna(axis=0, how="all", inplace=True)

            self.data_frame.drop_duplicates(keep="first", inplace=True)

            return True
        except ValueError:
            print(f"{self.path} - tabela vazia, " "certificados não gerados!!!")
            return False
        except KeyError:
            print(
                f'{self.path} - coluna "Informações" inexistente, '
                "certificados não gerados!!!"
            )
            return False

    def separar_tabela(self, data_frame):
        """
        Divide o dataframe de entrada em duas partes: uma com as informações
        gerais e outra com as funções. Além disso, remove valores nulos das
        colunas.

        Args: data_frame (pandas.DataFrame): Dataframe a ser separado em
        informações e funções

        Atribuições: data_frame_informacoes (pandas.DataFrame): Dataframe
        com as informações gerais data_frame_funcao (pandas.DataFrame):
        Dataframe com as funções
        """

        self.data_frame_informacoes = data_frame[["Informações"]].copy()
        self.data_frame_informacoes.dropna(axis=0, how="all", inplace=True)
        self.data_frame.drop(columns=["Informações"], inplace=True)
        self.data_frame_funcao = data_frame[["Função"]].copy()
        self.data_frame_funcao.dropna(axis=0, how="all", inplace=True)
        self.data_frame_funcao.drop_duplicates(keep="first", inplace=True)

    def get_data_frame(self):
        """Retorna a tabela completa"""
        return self.data_frame

    def get_data_frame_informacoes(self):
        """Retorna a tabela com as informações do evento"""
        return self.data_frame_informacoes

    def verificar_tab_padrao(self, folder_destino):
        """
        Verifica se a tabela é padrão e cria a pasta e subpastas para
        armazenar os certificados

        Parameters: folder_destino (str): Caminho da pasta de destino,
        utilizado para criar subpastas.
        """

        self.path_destino = folder_destino
        try:
            # pylint: disable=unused-variable
            dados_padrao = {  # noqa
                "nome_participante": self.data_frame["Nome"],
                "cpf_participante": self.data_frame["CPF"],
                "cargo_participante": self.data_frame["Função"],
                "frequencia_participante": self.data_frame["Frequência"],
                "nome_evento": self.data_frame_informacoes.iloc[0, 0],
                "carga_hor": self.data_frame_informacoes.iloc[1, 0],
                "nome_prof": self.data_frame_informacoes.iloc[2, 0],
                "nome_dep": self.data_frame_informacoes.iloc[3, 0],
                "data_inicial": self.data_frame_informacoes.iloc[4, 0],
                "data_final": self.data_frame_informacoes.iloc[5, 0],
                "nome_decano": self.data_frame_informacoes.iloc[6, 0],
            }
            # pylint: enable=unused-variable
            self.gerar_pasta_subpastas_cert()
            return True
        except KeyError:
            print(
                f'{self.path} - nem todos os campos da coluna " Informações "'
                "estão preenchidos, certificados não gerados!!!"
            )
            return False
        except IndexError:
            print(
                f"{self.path} - coluna está faltando, " "certificados não " "gerados!!!"
            )
            return False
