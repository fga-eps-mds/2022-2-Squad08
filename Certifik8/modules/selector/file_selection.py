import subprocess
import sys


class FileSelection:
    """
    Classe responsável por selecionar arquivos utilizando o zenity.

    Atributos:
        command (list): Lista de comandos para o zenity.
    """

    def __init__(self):
        """
        Inicializa a classe com o comando para executar o diálogo de seleção
        de arquivos.
        """

        self.command = ["zenity", "--file-selection", "--multiple"]

    def run(self):
        """
        Método responsável por rodar o comando do zenity e retornar a lista
        de nomes de arquivos selecionados.

        Retorna:
            list: Lista de nomes de arquivos selecionados.

        Lança:
            Exception: Se ocorrer algum erro inesperado.
        """

        try:
            zenity = subprocess.run(self.command, capture_output=True, check=False)

            filenames = str(zenity.stdout.decode("utf-8"))
            filenames = filenames.split("|")
            filenames[-1] = filenames[-1].replace("\n", "")
            return filenames
        except Exception:
            print("Ocorreu um erro inesperado!!!")
            sys.exit()
