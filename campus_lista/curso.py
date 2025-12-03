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
        if not isinstance(codigo, int):
            raise TypeError(f"Código deve ser int, recebido: {type(codigo).__name__}")
        if not isinstance(nome, str):
            raise TypeError(f"Nome deve ser str, recebido: {type(nome).__name__}")
        
        self.codigo = codigo
        self.nome = nome

    def atualizar_nome(self, novo_nome: str):
        if not isinstance(novo_nome, str):
            raise TypeError(f"Nome deve ser str, recebido: {type(novo_nome).__name__}")
        self.nome = novo_nome

    def __str__(self):
        return f"{self.__class__.__name__} {self.codigo} | Nome: {self.nome}"


class Curso(EntidadeAcademica):
    def __init__(self, codigo: int, nome: str, carga_horaria: int):
        super().__init__(codigo, nome)
        
        if not isinstance(carga_horaria, int):
            raise TypeError(f"Carga horária deve ser int, recebido: {type(carga_horaria).__name__}")
        if carga_horaria < 0:
            raise ValueError(f"Carga horária não pode ser negativa: {carga_horaria}")
        
        self.carga_horaria = carga_horaria

    def atualizar_ch(self, nova_ch: int):
        if not isinstance(nova_ch, int):
            raise TypeError(f"Carga horária deve ser int, recebido: {type(nova_ch).__name__}")
        if nova_ch < 0:
            raise ValueError(f"Carga horária não pode ser negativa: {nova_ch}")
        self.carga_horaria = nova_ch

    def __str__(self):
        return f"{super().__str__()} | CH: {self.carga_horaria}h"
