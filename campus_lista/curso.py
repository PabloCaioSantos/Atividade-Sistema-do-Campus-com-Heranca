{"id":"37192","variant":"standard","title":"curso.py — com herança"}
"""
arquivo: curso.py
-----------------
Implementa o conceito de Herança.

EntidadeAcademica:
    Classe base para qualquer entidade com código e nome.

Curso:
    Classe filha que herda de EntidadeAcademica e adiciona carga horária.
"""

class EntidadeAcademica:
    def __init__(self, codigo: int, nome: str):
        self.codigo = codigo
        self.nome = nome

    def atualizar_nome(self, novo_nome: str):
        self.nome = novo_nome

    def __str__(self):
        return f"{self.__class__.__name__} {self.codigo} | Nome: {self.nome}"


class Curso(EntidadeAcademica):
    def __init__(self, codigo: int, nome: str, carga_horaria: int):
        super().__init__(codigo, nome)
        self.carga_horaria = carga_horaria

    def atualizar_ch(self, nova_ch: int):
        self.carga_horaria = nova_ch

    def __str__(self):
        return f"{super().__str__()} | CH: {self.carga_horaria}h"
