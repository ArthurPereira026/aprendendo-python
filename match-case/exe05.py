while True:
    acesso = input("Digite o seu nível de usuário: ").upper()
    match acesso:
        case "ADMIN":
            print("Acesso Total: Ler, Criar, Deletar e Atualizar")
        case "GERENTE":
            print("Acesso Gerencial: Ler, Criar e Atualizar")
        case "EDITOR":
            print("Acesso de conteúdo: Ler e atualizar")
        case "VISITANTE":
            print("Acesso restrito: Apenas Ler")
        case _:
            print("Perfil não Reconhecido, Acesso bloqueado")
            break
