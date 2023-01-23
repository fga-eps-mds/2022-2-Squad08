import os
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

    def convert(self, output_name, foldername) -> None:
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads/")

        self.new_path = download_folder + f"{foldername}"
        if not os.path.exists(self.new_path):
            os.makedirs(self.new_path)

        try:
            pdfkit.from_file(
                self.html2pdf,
                self.new_path + f"/{output_name}.pdf",
                options=self.options,
            )
        except Exception:
            return False

        return True
