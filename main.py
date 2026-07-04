from seed import criar_banco, inserir_dados
from queries import (
    total_funcionarios_por_departamento,
    media_salarial_geral,
    top_10_maiores_salarios,
    funcionarios_acima_media,
)


def exibir_resultados():
    print("\nTotal de funcionários por departamento")
    for item in total_funcionarios_por_departamento():
        print(item)

    print("\nMédia salarial geral")
    print(media_salarial_geral())

    print("\nTop 10 maiores salários")
    for item in top_10_maiores_salarios():
        print(item)

    print("\nFuncionários acima da média")
    for item in funcionarios_acima_media():
        print(item)


def executar(carregar_dados=False):
    criar_banco()

    if carregar_dados:
        inserir_dados()

    exibir_resultados()


if __name__ == "__main__":
    executar(carregar_dados=False)