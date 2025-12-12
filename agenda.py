# Adicionar Contato
def adicionar_contato(contatos):
    print("\n--- Adicionar Contato ---")
    nome = input("Nome do contato: ")
    telefone = input("Telefone do contato: ")
    email = input("Email do contato: ")
    favorito = input("Marcar como favorito? (Sim/Não): ").lower() == "sim"

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }
    contatos.append(contato)
    print(f"Contato '{nome}' adicionado com sucesso!")
    return

# Visualizar a lista de contatos
def ver_contatos(contatos):
    print("\n--- Lista de Contatos ---")
    for indice, contato in enumerate(contatos, start=1):
        status_favorito = "★" if contato["favorito"] else " "
        print(f"{indice}. [{status_favorito}] Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    return

# Editar um contato
def editar_contato(contatos, indice_contato):
    indice_ajustado = int(indice_contato) - 1
    if 0 <= indice_ajustado < len(contatos):
        print("\n--- Editar Contato ---")
        print(f"Editando contato: {contatos[indice_ajustado]['nome']}")
        novo_nome = input("Novo nome (deixe em branco para não alterar): ")
        novo_telefone = input("Novo telefone (deixe em branco para não alterar): ")
        novo_email = input("Novo email (deixe em branco para não alterar): ")
        novo_favorito = input("Marcar como favorito? (sim/não) (deixe em branco para não alterar): ").lower()

        if novo_nome:
            contatos[indice_ajustado]["nome"] = novo_nome
        if novo_telefone:
            contatos[indice_ajustado]["telefone"] = novo_telefone
        if novo_email:
            contatos[indice_ajustado]["email"] = novo_email
        if novo_favorito:
            contatos[indice_ajustado]["favorito"] = novo_favorito == "sim"

        print("Contato atualizado com sucesso!")
    else:
        print("Índice inválido. Contato não encontrado.")
    return

# Marcar/desmarcar um contato como favorito
def toggle_favorito(contatos, indice_contato):
    indice_ajustado = int(indice_contato) - 1
    if 0 <= indice_ajustado < len(contatos):
        contatos[indice_ajustado]["favorito"] = not contatos[indice_ajustado]["favorito"]
        status = "favoritado" if contatos[indice_ajustado]["favorito"] else "desfavoritado"
        print(f"Contato '{contatos[indice_ajustado]['nome']}' {status} com sucesso!")
    else:
        print("Índice inválido. Contato não encontrado.")
    return

# Visualizar contatos favoritos
def ver_favoritos(contatos):
    print("\n--- Contatos Favoritos ---")
    favoritos = [contato for contato in contatos if contato["favorito"]]
    if favoritos:
        for indice, contato in enumerate(favoritos, start=1):
            print(f"{indice}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    else:
        print("Nenhum contato favorito encontrado.")
    return

# Deletar um contato
def deletar_contato(contatos, indice_contato):
    indice_ajustado = int(indice_contato) - 1
    if 0 <= indice_ajustado < len(contatos):
        contato_removido = contatos.pop(indice_ajustado)
        print(f"Contato '{contato_removido['nome']}' removido com sucesso!")
    else:
        print("Índice inválido. Contato não encontrado.")
    return

# Código Principal
def main():
    contatos = []
    while True:
        print("\n--- Menu de Contatos ---")
        print("1. Adicionar contato")
        print("2. Ver contatos")
        print("3. Editar contato")
        print("4. Marcar/Desmarcar como favorito")
        print("5. Ver contatos favoritos")
        print("6. Deletar contato")
        print("7. Sair")

        escolha = input("Digite a sua escolha: ")

        if escolha == "1":
            adicionar_contato(contatos)
        elif escolha == "2":
            ver_contatos(contatos)
        elif escolha == "3":
            ver_contatos(contatos)
            indice_contato = input("Digite o número do contato que deseja editar: ")
            editar_contato(contatos, indice_contato)
        elif escolha == "4":
            ver_contatos(contatos)
            indice_contato = input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")
            toggle_favorito(contatos, indice_contato)
        elif escolha == "5":
            ver_favoritos(contatos)
        elif escolha == "6":
            ver_contatos(contatos)
            indice_contato = input("Digite o número do contato que deseja deletar: ")
            deletar_contato(contatos, indice_contato)
        elif escolha == "7":
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")

# Execução
if __name__ == "__main__":
    main()
