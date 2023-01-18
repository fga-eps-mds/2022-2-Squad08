import os
import pdfkit
from ..utils import get_download_path


class Html2Pdf:

    def __init__(self, html="template/template.html"):
        self.html2pdf = html
        self.options = {
            "page-size": "A5",
            "orientation": "landscape",
            "encoding": "UTF-8",
        }
        self.new_path = ""

    def create_folder(self):
        os.makedirs(self.new_path)

    def convert(self, output_name, foldername) -> None:
        download_folder = get_download_path()

        self.new_path = download_folder + f"{foldername}"
        if not os.path.exists(self.new_path):
            self.create_folder()

        pdfkit.from_file(
            self.html2pdf,
            self.new_path + f"/{output_name}.pdf",
            options=self.options,
        )
