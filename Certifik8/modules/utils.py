from datetime import date

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
    dia = date.today().strftime("%d")
    mes = int(date.today().strftime("%m")) - 1
    ano = date.today().strftime("%Y")
    return f"{dia} de {meses[mes]} de {ano}"


def get_foldername(filepath):
    return filepath.split("/")[-1].split(".")[0]
