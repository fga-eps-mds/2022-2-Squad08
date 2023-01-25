import subprocess


class FolderSelection:

    def __init__(self):
        self.command = ["zenity", "--file-selection", "--directory"]

    def run(self):
        try:
            zenity = subprocess.run(self.command, capture_output=True, check=False)

            if zenity.returncode not in (0, 1):
                return False

            foldername = str(zenity.stdout.decode("utf-8"))
            foldername = foldername.replace("\n", "")
            return foldername
        except Exception:
            return False
