# Sistema do Campus com Herança  
Atividade da disciplina Programação Orientada a Objetos  
Curso: Análise e Desenvolvimento de Sistemas — Universidade Federal do Ceará (UFC)

## Introdução
Este projeto tem como objetivo demonstrar, de forma prática, a aplicação do princípio de herança dentro da Programação Orientada a Objetos (POO).  
A atividade consiste em implementar um sistema simples de gerenciamento de Campi e Cursos da UFC, inicialmente estruturado com classes independentes e posteriormente refatorado para incluir generalização e especialização entre classes.

Este README apresenta:
- Onde a herança foi aplicada  
- Como as classes se relacionam  
- O funcionamento geral do sistema  
- Como executar o projeto  

---

## Aplicação do Conceito de Herança

A herança permite criar uma estrutura hierárquica onde classes compartilham atributos e comportamentos comuns. Isso reduz repetição, melhora organização e facilita a manutenção do código.

No projeto, o conceito foi aplicado da seguinte forma:

### Classe Base: EntidadeAcadêmica
Representa qualquer entidade que possua código identificador e nome.  
Ela fornece atributos e métodos básicos para todas as classes que a herdam.

Exemplo de uso da herança:
- A classe Curso herda de EntidadeAcadêmica, obtendo automaticamente código e nome.

### Classe Base: GerenciadorLista
Responsável por fornecer funcionalidades genéricas de gerenciamento de listas, como adicionar, remover, listar e buscar elementos.  
Qualquer classe que necessite manipular coleções pode herdar dessa estrutura.

Exemplo de uso da herança:
- A classe CampusLista herda de GerenciadorLista, aplicando o comportamento de gerenciamento de cursos.

---

## Classe Derivada: Curso
A classe Curso passa a herdar os atributos código e nome da classe EntidadeAcadêmica.  
Ela se especializa adicionando a carga horária e métodos específicos relacionados ao curso.

---

## Classe Derivada: CampusLista
A classe CampusLista herda métodos de gerenciamento de itens da classe GerenciadorLista.  
Dentro do contexto do projeto, ela gerencia cursos, permitindo:
- Cadastro de novos cursos  
- Listagem dos cursos existentes  
- Atualização de dados  
- Remoção de cursos  

---

## Estrutura Simplificada do Projeto

```
campus_lista/
│── __init__.py
│── curso.py
│── campus_lista.py
main.py
README.md
```

---

## Como Executar o Sistema

1. Certifique-se de possuir Python versão 3.8 ou superior.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

```
python main.py
```

4. O menu será exibido com as opções de criação de campi, seleção de campus, cadastro de cursos e demais funcionalidades.

---

## Conclusão

A refatoração realizada demonstra de forma clara a aplicação do princípio de herança na Programação Orientada a Objetos.  
Com a criação de classes-base e a especialização das classes derivadas, o código se torna mais organizado, reutilizável e coerente com os princípios estudados em sala.

O sistema final apresenta uma arquitetura mais limpa e preparada para futuras expansões.
