{"id":"37195","variant":"standard","title":"main.py — compatível com herança"}
"""
arquivo: main.py
----------------
Arquivo de entrada do sistema para gerenciar campi e cursos.
Funciona com o novo modelo baseado em herança.
"""

from campus_lista import CampusLista


def menu():
    print("\n====== Sistema UFC ======")
    print("1 - Criar Campus")
    print("2 - Selecionar Campus")
    print("3 - Listar Campi")
    print("0 - Sair")
    return input("Escolha: ")


def menu_campus(campus):
    if not isinstance(campus, CampusLista):
        raise TypeError(f"Esperado CampusLista, recebido: {type(campus).__name__}")
    
    while True:
        print(f"\n--- Campus: {campus.nome} ---")
        print("1 - Cadastrar curso")
        print("2 - Listar cursos")
        print("3 - Atualizar curso")
        print("4 - Remover curso")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                nome = input("Nome do curso: ")
                ch = int(input("Carga horária: "))
                campus.cadastrar_curso(nome, ch)
            except (ValueError, TypeError) as e:
                print(f"[ERRO] Entrada inválida: {e}")

        elif opcao == "2":
            campus.listar_cursos()

        elif opcao == "3":
            try:
                codigo = int(input("Código do curso: "))
                novo_nome = input("Novo nome (ou ENTER): ")
                nova_ch = input("Nova CH (ou ENTER): ")

                campus.atualizar_curso(
                    codigo,
                    novo_nome if novo_nome else None,
                    int(nova_ch) if nova_ch else None
                )
            except (ValueError, TypeError) as e:
                print(f"[ERRO] Entrada inválida: {e}")

        elif opcao == "4":
            try:
                codigo = int(input("Código do curso a remover: "))
                campus.remover_curso(codigo)
            except (ValueError, TypeError) as e:
                print(f"[ERRO] Entrada inválida: {e}")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def main():
    campi = []

    while True:
        opcao = menu()

        if opcao == "1":
            try:
                nome = input("Nome do novo campus: ")
                campus = CampusLista(nome)
                if not isinstance(campus, CampusLista):
                    raise TypeError("Falha ao criar CampusLista")
                campi.append(campus)
                print(f"[OK] Campus '{nome}' criado!")
            except (ValueError, TypeError) as e:
                print(f"[ERRO] Não foi possível criar campus: {e}")

        elif opcao == "2":
            if not campi:
                print("Nenhum campus cadastrado.")
                continue

            try:
                for i, c in enumerate(campi, start=1):
                    if isinstance(c, CampusLista):
                        print(f"{i} - {c.nome}")

                escolha = int(input("Escolha o campus: ")) - 1

                if 0 <= escolha < len(campi):
                    campus_selecionado = campi[escolha]
                    if isinstance(campus_selecionado, CampusLista):
                        menu_campus(campus_selecionado)
                    else:
                        print("[ERRO] Item não é um campus válido.")
                else:
                    print("Campus inválido.")
            except (ValueError, TypeError, IndexError) as e:
                print(f"[ERRO] Seleção inválida: {e}")

        elif opcao == "3":
            if not campi:
                print("Nenhum campus cadastrado.")
            else:
                for c in campi:
                    if isinstance(c, CampusLista):
                        print(c)
                    else:
                        print(f"[AVISO] Item inválido encontrado: {type(c).__name__}")

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
