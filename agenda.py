def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionada com sucesso!")
    return

def ver_contato(contatos):
    print("\nLista de contatos")
    for indice, contato in enumerate(contatos, start=1):
        favorito_contato = "☆" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"\n{indice}.Contato:")
        print(f"Nome: {nome_contato}")
        print(f"Telefone: {telefone_contato}")
        print(f"Email: {email_contato}")
        print(f"Favorito: {favorito_contato}")
    return

def atualizar_nome_contato(contatos, indice_contato, novo_nome_contato):
    indice_tarefa_ajustado = int(indice_contato) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(contatos):
        contatos[indice_tarefa_ajustado]["nome"] = novo_nome_contato
        print(f"Nome do contato {indice_contato} atualizada para {novo_nome_contato}")
    else:
        print("Indice de contato invalido")
    return 

def atualizar_telefone_contato(contatos, indice_contato, novo_telefone_contato):
    indice_tarefa_ajustado = int(indice_contato) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(contatos):
        contatos[indice_tarefa_ajustado]["telefone"] = novo_telefone_contato
        print(f"Telefone do contato {indice_contato} atualizada para {novo_telefone_contato}")
    else:
        print("Indice de contato invalido")
    return 

def atualizar_email_contato(contatos, indice_contato, novo_email_contato):
    indice_tarefa_ajustado = int(indice_contato) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(contatos):
        contatos[indice_tarefa_ajustado]["nome"] = novo_email_contato
        print(f"Email do contato {indice_contato} atualizada para {novo_email_contato}")
    else:
        print("Indice de contato invalido")
    return 

def favoritar_desvaforitar_contato(contatos, indice_contato):
    indice_tarefa_ajustado = int(indice_contato) - 1
    if contatos[indice_tarefa_ajustado]["favorito"] == False:
        contatos[indice_tarefa_ajustado]["favorito"] = True
        print(f"Contato {indice_contato} Favoritado!")
    else:
        contatos[indice_tarefa_ajustado]["favorito"] = False
        print(f"Contato {indice_contato} Desfavoritado!")
    return

def contatos_favoritos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            nome_contato = contato["nome"]
            telefone_contato = contato["telefone"]
            email_contato = contato["email"]
            favorito_contato = "☆"
            print(f"{indice}. Nome: {nome_contato} \
            Telefone: {telefone_contato} \
            Email: {email_contato} \
            Favorito: {favorito_contato}")
    return

def deletar_contato(contatos, indice_contato):
    for indice_contato in contatos:
        contatos.remove(indice_contato)
        print("Contato Deletado!")
    return 

contatos = []

while True:
    print("\n Menu do Gerenciado da Lista de Tarefas:")
    print("1. Adicionar Contato")
    print("2. Ver Contato")
    print("3. Editar Contato")
    print("4. Favoritar ou Desfavoritar Contato")
    print("5. Lista de Contatos Favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = input("Digite a sua escolha:")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato: ")
        telefone_contato = input("Digite o telefone do contato: ")
        email_contato = input("Digite o e-mail do contato: ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    elif escolha == "2":
        ver_contato(contatos)
    elif escolha =="3":
        ver_contato(contatos)
        indice_contato = input("Qual contato deseja editar: ")
        while True:
            print("\n Menu de edição:")
            print("1. Editar nome")
            print("2. Editar telefone")
            print("3. Editar email")
            print("4. Sauir e salvar")
            escolha = input("Digite a sua escolha:")
            if escolha == "1":
                print("Qual o novo nome")
                novo_nome_contato = input("Digite o novo nome do contato: ")
                atualizar_nome_contato(contatos, indice_contato, novo_nome_contato)
            elif escolha == "2":
                print("Qual o novo telefone")
                novo_telefone_contato = input("Digite o novo telefone do contato: ")
                atualizar_telefone_contato(contatos, indice_contato, novo_telefone_contato)
            elif escolha == "3":
                print("Qual o novo email")
                novo_email_contato = input("Digite o novo email do contato: ")
                atualizar_email_contato(contatos, indice_contato, novo_email_contato)
            elif escolha == "4":
                break 
    elif escolha == "4":
        ver_contato(contatos)
        indice_contato = input("Qual contato deseja favoritar ou desfavoritar: ")
        favoritar_desvaforitar_contato(contatos, indice_contato)
    elif escolha =="5":
        contatos_favoritos(contatos)
    elif escolha == "6":
        ver_contato(contatos)
        indice_contato = input("Qual contato deseja deletar:")
        deletar_contato(contatos, indice_contato)        
    elif escolha == "7":
        break
print("Programa Finalizado")