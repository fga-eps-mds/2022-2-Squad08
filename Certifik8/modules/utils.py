from datetime import date
import os

meses = (
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
)


def get_data() -> str:
    """
    Obtém a data atual formatada como "dd de mês de aaaa".

    Returns:
        str: Data atual formatada.
    """

    dia = date.today().strftime("%d")
    mes = int(date.today().strftime("%m")) - 1
    ano = date.today().strftime("%Y")
    return f"{dia} de {meses[mes]} de {ano}"


def get_foldername(filepath: str) -> str:
    """
    Obtém o nome do diretório a partir do caminho completo do arquivo.

    Args:
        filepath (str): Caminho completo do arquivo.

    Returns:
        str: Nome do diretório.
    """

    return filepath.split("/")[-1].split(".")[0]


def verificar_xlsx(path: str) -> bool:
    """
    Verifica se um caminho específico corresponde a um arquivo xlsx válido.

    Args:
        path (str): Caminho do arquivo.

    Returns:
        bool: Verdadeiro se o caminho corresponde a um arquivo xlsx,
        falso caso contrário.
    """

    return os.path.exists(path) and os.path.splitext(path)[1] == ".xlsx"
