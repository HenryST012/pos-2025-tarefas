import users

def menu():
    while True:
        print("\n===== MENU - API USERS =====")
        print("1. Listar usuários")
        print("2. Ler usuário por ID")
        print("3. Criar novo usuário")
        print("4. Atualizar usuário")
        print("5. Deletar usuário")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lista = users.list()
            for u in lista:
                print(f"{u['id']} - {u['name']} ({u['email']})")
        
        elif opcao == "2":
            user_id = input("Digite o ID do usuário: ")
            user = users.read(user_id)
            print(user)

        elif opcao == "3":
            nome = input("Nome: ")
            email = input("Email: ")
            user = users.create({"name": nome, "email": email})
            print("Usuário criado:", user)

        elif opcao == "4":
            user_id = input("ID do usuário a atualizar: ")
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            user = users.update(user_id, {"name": nome, "email": email})
            print("Usuário atualizado:", user)

        elif opcao == "5":
            user_id = input("ID do usuário a deletar: ")
            resultado = users.delete(user_id)
            print("Resultado:", resultado)

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
