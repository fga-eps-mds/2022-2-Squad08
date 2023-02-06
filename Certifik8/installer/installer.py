import subprocess


def installer():
    """
    Instala dependências necessárias para o funcionamento da aplicação.
    """

    comando = ["./dependencies.sh"]
    subprocess.call(comando)
