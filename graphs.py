from pathlib import Path

import matplotlib.pyplot as plt

from queries import (
    funcionarios_acima_media,
    media_salarial_geral,
    top_10_maiores_salarios,
    total_funcionarios_por_departamento,
)


PASTA_PROJETO = Path(__file__).resolve().parent
PASTA_GRAFICOS = PASTA_PROJETO / "graficos"


def _criar_pasta_graficos():
    PASTA_GRAFICOS.mkdir(exist_ok=True)


def _formatar_moeda(valor):
    return f"R$ {float(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _tem_dados(dados, nome_analise):
    if dados:
        return True

    print(f"Nenhum dado encontrado para gerar o gráfico: {nome_analise}.")
    return False


def grafico_total_funcionarios_por_departamento():
    _criar_pasta_graficos()
    dados = total_funcionarios_por_departamento()
    if not _tem_dados(dados, "total de funcionários por departamento"):
        return

    departamentos = [item.departamento for item in dados]
    totais = [item.total_funcionarios for item in dados]

    plt.figure(figsize=(10, 6))
    barras = plt.bar(departamentos, totais, color="#2F80ED")

    plt.title("Total de Funcionários por Departamento")
    plt.xlabel("Departamento")
    plt.ylabel("Total de Funcionários")
    plt.xticks(rotation=30, ha="right")
    plt.bar_label(barras)
    plt.tight_layout()

    caminho = PASTA_GRAFICOS / "total_funcionarios_por_departamento.png"
    plt.savefig(caminho, dpi=300)
    plt.show()


def grafico_top_10_maiores_salarios():
    _criar_pasta_graficos()
    dados = top_10_maiores_salarios()
    if not _tem_dados(dados, "top 10 maiores salários"):
        return

    nomes = [item.nome for item in dados]
    salarios = [float(item.salario_atual) for item in dados]

    plt.figure(figsize=(10, 6))
    barras = plt.barh(nomes, salarios, color="#27AE60")

    plt.title("Top 10 Maiores Salários")
    plt.xlabel("Salário Atual")
    plt.ylabel("Funcionário")
    plt.gca().invert_yaxis()

    for barra, salario in zip(barras, salarios):
        plt.text(
            barra.get_width(),
            barra.get_y() + barra.get_height() / 2,
            f" {_formatar_moeda(salario)}",
            va="center",
        )

    plt.tight_layout()

    caminho = PASTA_GRAFICOS / "top_10_maiores_salarios.png"
    plt.savefig(caminho, dpi=300)
    plt.show()


def grafico_funcionarios_acima_media():
    _criar_pasta_graficos()
    dados = funcionarios_acima_media()
    if not _tem_dados(dados, "funcionários acima da média"):
        return

    media = float(media_salarial_geral())

    nomes = [item.nome for item in dados]
    salarios = [float(item.salario_atual) for item in dados]

    plt.figure(figsize=(10, 6))
    barras = plt.bar(nomes, salarios, color="#F2994A")

    plt.axhline(
        media,
        color="#EB5757",
        linestyle="--",
        linewidth=2,
        label=f"Média geral: {_formatar_moeda(media)}",
    )

    plt.title("Funcionários com Salário Acima da Média")
    plt.xlabel("Funcionário")
    plt.ylabel("Salário Atual")
    plt.xticks(rotation=30, ha="right")
    plt.legend()

    for barra, salario in zip(barras, salarios):
        plt.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height(),
            _formatar_moeda(salario),
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.tight_layout()

    caminho = PASTA_GRAFICOS / "funcionarios_acima_media.png"
    plt.savefig(caminho, dpi=300)
    plt.show()


def gerar_todos_os_graficos():
    _criar_pasta_graficos()
    grafico_total_funcionarios_por_departamento()
    grafico_top_10_maiores_salarios()
    grafico_funcionarios_acima_media()


if __name__ == "__main__":
    gerar_todos_os_graficos()
