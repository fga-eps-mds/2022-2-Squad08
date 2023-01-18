import os
import pdfkit


def get_download_path():
    return os.path.join(os.path.expanduser("~"), "Downloads/")


class Html2Pdf:
    options = {
        "page-size": "A5",
        "orientation": "landscape",
        "encoding": "UTF-8",
    }

    new_path = ''

    def __init__(self, html="template/template.html"):
        self.html2pdf = html

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
