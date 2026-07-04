from datetime import date
from database import SessionLocal, Base, engine
from models import Departamento, Cargo, Funcionario, HistoricoPromocao


def criar_banco():
    Base.metadata.create_all(bind=engine)


def inserir_dados():
    session = SessionLocal()

    departamentos = [
        Departamento(nome="Tecnologia", descricao="Área de tecnologia e dados"),
        Departamento(nome="Financeiro", descricao="Área financeira"),
        Departamento(nome="Recursos Humanos", descricao="Gestão de pessoas"),
        Departamento(nome="Vendas", descricao="Área comercial"),
        Departamento(nome="Operações", descricao="Área operacional"),
    ]

    cargos = [
        Cargo(titulo="Analista de Dados", nivel="Pleno", salario_base=6500),
        Cargo(titulo="Engenheiro de Dados", nivel="Sênior", salario_base=12000),
        Cargo(titulo="Analista Financeiro", nivel="Pleno", salario_base=5500),
        Cargo(titulo="Analista de RH", nivel="Júnior", salario_base=3500),
        Cargo(titulo="Coordenador Comercial", nivel="Sênior", salario_base=9000),
    ]

    session.add_all(departamentos)
    session.add_all(cargos)
    session.commit()

    funcionarios = [
        Funcionario(
            nome="Daniel Augusto Gomes",
            email="daniel.gomes@email.com",
            salario_atual=8500,
            data_admissao=date(2021, 3, 15),
            status="ativo",
            cidade="Joinville",
            estado="SC",
            departamento_id=1,
            cargo_id=1,
        ),
        Funcionario(
            nome="Ana Beatriz Costa",
            email="ana.costa@email.com",
            salario_atual=12500,
            data_admissao=date(2019, 8, 10),
            status="ativo",
            cidade="Curitiba",
            estado="PR",
            departamento_id=1,
            cargo_id=2,
        ),
        Funcionario(
            nome="Bruno Mendes",
            email="bruno.mendes@email.com",
            salario_atual=6200,
            data_admissao=date(2020, 5, 20),
            status="ativo",
            cidade="São Paulo",
            estado="SP",
            departamento_id=2,
            cargo_id=3,
        ),
        Funcionario(
            nome="Carla Souza",
            email="carla.souza@email.com",
            salario_atual=3900,
            data_admissao=date(2022, 1, 12),
            status="ativo",
            cidade="Florianópolis",
            estado="SC",
            departamento_id=3,
            cargo_id=4,
        ),
        Funcionario(
            nome="Eduardo Lima",
            email="eduardo.lima@email.com",
            salario_atual=9700,
            data_admissao=date(2018, 11, 5),
            status="desligado",
            data_demissao=date(2024, 2, 20),
            cidade="Rio de Janeiro",
            estado="RJ",
            departamento_id=4,
            cargo_id=5,
        ),
    ]

    session.add_all(funcionarios)
    session.commit()

    promocoes = [
        HistoricoPromocao(
            funcionario_id=1,
            cargo_anterior_id=4,
            cargo_novo_id=1,
            data_promocao=date(2023, 6, 1),
            aumento_percentual=18.5,
            motivo="Evolução técnica e entrega de projetos",
        ),
        HistoricoPromocao(
            funcionario_id=2,
            cargo_anterior_id=1,
            cargo_novo_id=2,
            data_promocao=date(2022, 9, 1),
            aumento_percentual=25.0,
            motivo="Promoção para posição sênior",
        ),
    ]

    session.add_all(promocoes)
    session.commit()
    session.close()


if __name__ == "__main__":
    criar_banco()
    inserir_dados()