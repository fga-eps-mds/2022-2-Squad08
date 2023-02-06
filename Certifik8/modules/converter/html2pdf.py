import pdfkit


class Html2Pdf:
    """
    Uma classe para converter HTML para PDF.

    Atributos:
        html2pdf (str): Caminho para o arquivo HTML a ser convertido.
        options (dict): Dicionário de opções para configurar a saída PDF.
        new_path (str): O novo caminho do arquivo PDF gerado.

    Métodos:
        convert(output_name, foldername, folder_destino, output_funcao):
            Converte o arquivo HTML em PDF
            e o salva no caminho especificado.
    """

    def __init__(self, html):
        """
        Construtor da classe Html2Pdf.

        Args:
            html (str): Caminho para o arquivo HTML a ser convertido.
        """

        self.html2pdf = html
        self.options = {
            "page-size": "A5",
            "orientation": "landscape",
            "encoding": "UTF-8",
        }
        self.new_path = ""

    def convert(self, output_name, foldername, folder_destino, output_funcao) -> None:
        """
        Converte o arquivo HTML em PDF e o salva no caminho especificado.

        Args: output_name (str): O nome do arquivo PDF de saída. foldername
        (str): O nome da pasta para salvar o arquivo PDF. folder_destino (
        str): A pasta de destino para salvar o arquivo PDF. output_funcao (
        str): A função de saída a ser usada no nome do arquivo.

        Retorna: bool: Verdadeiro se a conversão for bem-sucedida, Falso
        caso contrário.
        """

        self.new_path = folder_destino + "/" + f"{foldername}" + "/" + output_funcao
        try:
            pdfkit.from_file(
                self.html2pdf,
                self.new_path + f"/{output_name}.pdf",
                options=self.options,
            )
            return True
        except Exception:
            return False
