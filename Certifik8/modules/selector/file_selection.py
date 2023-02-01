import subprocess


class FileSelection:
    def __init__(self):
        self.command = ["zenity", "--file-selection", "--multiple"]

    def run(self):
        try:
            zenity = subprocess.run(self.command, capture_output=True, check=False)

            if zenity.returncode not in (0, 1):
                return False

            filenames = str(zenity.stdout.decode("utf-8"))
            filenames = filenames.split("|")
            filenames[-1] = filenames[-1].replace("\n", "")
            return filenames
        except Exception:
            return False
