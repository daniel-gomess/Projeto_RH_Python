from sqlalchemy import func, desc
from database import SessionLocal
from models import Departamento, Cargo, Funcionario, HistoricoPromocao


def total_funcionarios_por_departamento():
    session = SessionLocal()

    resultado = (
        session.query(
            Departamento.nome.label("departamento"),
            func.count(Funcionario.id).label("total_funcionarios")
        )
        .join(Funcionario, Funcionario.departamento_id == Departamento.id)
        .group_by(Departamento.nome)
        .order_by(desc("total_funcionarios"))
        .all()
    )

    session.close()
    return resultado


def media_salarial_geral():
    session = SessionLocal()

    resultado = session.query(
        func.avg(Funcionario.salario_atual).label("media_salarial")
    ).scalar()

    session.close()
    return resultado


def top_10_maiores_salarios():
    session = SessionLocal()

    resultado = (
        session.query(
            Funcionario.nome,
            Departamento.nome.label("departamento"),
            Cargo.titulo.label("cargo"),
            Funcionario.salario_atual
        )
        .join(Departamento, Departamento.id == Funcionario.departamento_id)
        .join(Cargo, Cargo.id == Funcionario.cargo_id)
        .order_by(Funcionario.salario_atual.desc())
        .limit(10)
        .all()
    )

    session.close()
    return resultado


def funcionarios_acima_media():
    session = SessionLocal()

    media = session.query(func.avg(Funcionario.salario_atual)).scalar()

    resultado = (
        session.query(Funcionario.nome, Funcionario.salario_atual)
        .filter(Funcionario.salario_atual > media)
        .order_by(Funcionario.salario_atual.desc())
        .all()
    )

    session.close()
    return resultado


def turnover_por_departamento():
    session = SessionLocal()

    resultado = (
        session.query(
            Departamento.nome.label("departamento"),
            func.count(Funcionario.id).label("total_funcionarios"),
            func.sum(
                func.case(
                    (Funcionario.status == "desligado", 1),
                    else_=0
                )
            ).label("total_desligados")
        )
        .outerjoin(Funcionario, Funcionario.departamento_id == Departamento.id)
        .group_by(Departamento.nome)
        .all()
    )

    session.close()
    return resultado