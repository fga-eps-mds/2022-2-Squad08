import subprocess
import sys


class FolderSelection:
    """
    Classe responsável por selecionar uma pasta utilizando o zenity.

    Atributos:
        command (list): Lista de comandos para o zenity.
    """

    def __init__(self):
        """
        Inicializa a classe com o comando para executar o diálogo de seleção
        de pasta.
        """

        self.command = ["zenity", "--file-selection", "--directory"]

    def run(self):
        """
        Executa o diálogo de seleção de pasta e retorna o caminho da pasta
        selecionada.

        Returns:
            str: O caminho da pasta selecionada.

        Raises: Exception: Se ocorrer um erro inesperado durante a execução
        do diálogo.
        """

        try:
            zenity = subprocess.run(self.command, capture_output=True, check=False)

            foldername = str(zenity.stdout.decode("utf-8"))
            foldername = foldername.replace("\n", "")
            return foldername
        except Exception:
            print("Ocorreu um erro inesperado!!!")
            sys.exit()
