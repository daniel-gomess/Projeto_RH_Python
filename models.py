from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Departamento(Base):
    __tablename__ = "departamentos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255))

    funcionarios = relationship("Funcionario", back_populates="departamento")


class Cargo(Base):
    __tablename__ = "cargos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    nivel = Column(String(50), nullable=False)
    salario_base = Column(Numeric(10, 2), nullable=False)

    funcionarios = relationship("Funcionario", back_populates="cargo")


class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    salario_atual = Column(Numeric(10, 2), nullable=False)
    data_admissao = Column(Date, nullable=False)
    data_demissao = Column(Date)
    status = Column(String(30), nullable=False)
    cidade = Column(String(100))
    estado = Column(String(2))

    departamento_id = Column(Integer, ForeignKey("departamentos.id"))
    cargo_id = Column(Integer, ForeignKey("cargos.id"))

    departamento = relationship("Departamento", back_populates="funcionarios")
    cargo = relationship("Cargo", back_populates="funcionarios")
    promocoes = relationship("HistoricoPromocao", back_populates="funcionario")


class HistoricoPromocao(Base):
    __tablename__ = "historico_promocoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"))
    cargo_anterior_id = Column(Integer, ForeignKey("cargos.id"))
    cargo_novo_id = Column(Integer, ForeignKey("cargos.id"))
    data_promocao = Column(Date, nullable=False)
    aumento_percentual = Column(Numeric(5, 2), nullable=False)
    motivo = Column(String(255))

    funcionario = relationship("Funcionario", back_populates="promocoes")
    cargo_anterior = relationship("Cargo", foreign_keys=[cargo_anterior_id])
    cargo_novo = relationship("Cargo", foreign_keys=[cargo_novo_id])