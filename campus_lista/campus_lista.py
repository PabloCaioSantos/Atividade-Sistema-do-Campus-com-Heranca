{"id":"37193","variant":"standard","title":"campus_lista.py — com herança"}
"""
arquivo: campus_lista.py
------------------------
Agora utiliza herança.

GerenciadorLista:
    Classe base genérica que implementa operações CRUD.

CampusLista:
    Classe filha especializada em gerenciar objetos do tipo Curso.
"""

from .curso import Curso


class GerenciadorLista:
    _id_global = 1  # ID automático para entidades

    def __init__(self):
        self.itens = []

    def cadastrar(self, item):
        item.codigo = GerenciadorLista._id_global
        GerenciadorLista._id_global += 1
        self.itens.append(item)
        print(f"[OK] Cadastro realizado:\n{item}")

    def listar(self):
        if not self.itens:
            print("Nenhum item cadastrado.")
            return
        for i in self.itens:
            print(i)

    def buscar(self, codigo: int):
        return next((i for i in self.itens if i.codigo == codigo), None)

    def atualizar(self, codigo: int, **kwargs):
        item = self.buscar(codigo)
        if not item:
            print("Item não encontrado.")
            return

        for atributo, valor in kwargs.items():
            if hasattr(item, atributo) and valor is not None:
                setattr(item, atributo, valor)

        print(f"[OK] Item atualizado:\n{item}")

    def remover(self, codigo: int):
        item = self.buscar(codigo)
        if item:
            self.itens.remove(item)
            print(f"[OK] Item removido: {codigo}")
        else:
            print("Item não encontrado.")


class CampusLista(GerenciadorLista):
    def __init__(self, nome: str):
        super().__init__()
        self.nome = nome

    def cadastrar_curso(self, nome: str, carga_horaria: int):
        curso = Curso(0, nome, carga_horaria)
        self.cadastrar(curso)

    def listar_cursos(self):
        self.listar()

    def procurar_curso(self, codigo: int):
        return self.buscar(codigo)

    def atualizar_curso(self, codigo: int, novo_nome=None, nova_ch=None):
        self.atualizar(
            codigo,
            nome=novo_nome if novo_nome else None,
            carga_horaria=nova_ch if nova_ch else None
        )

    def remover_curso(self, codigo: int):
        self.remover(codigo)

    def __str__(self):
        return f"Campus: {self.nome} | Total de Cursos: {len(self.itens)}"
