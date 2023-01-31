import pdfkit


class Html2Pdf:
    def __init__(self, html):
        self.html2pdf = html
        self.options = {
            "page-size": "A5",
            "orientation": "landscape",
            "encoding": "UTF-8",
        }
        self.new_path = ""

    def convert(self, output_name, foldername, folder_destino, output_funcao) -> None:

        self.new_path = folder_destino + "/" + f"{foldername}" + "/" + output_funcao
        try:
            pdfkit.from_file(
                self.html2pdf,
                self.new_path + f"/{output_name}.pdf",
                options=self.options,
            )
        except Exception:

            return False

        return True
