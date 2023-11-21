agenda=[]
while True:
    print("1- Cadastro")
    print('2 - Pesquisa pelo nome')
    print('3 - Listar')
    print('4 - Alterar')
    print('5- Excluir')
    opcao = int(input('Informe a opção: '))

    if opcao == 1:
        pessoa = {}
        pessoa['nome'] = input("Informe nome: ")
        pessoa['email'] = input("Informe email: ")
        pessoa['telefone'] = input("Informe telefone: ")
        agenda.append(pessoa)
    elif opcao == 2:
        nomebusca = input('Informe o nome para busca:')
        for elemento in agenda:
            if elemento['nome'].lower()== nomebusca.lower:
                print((f"""{elemento['nome']}\t")
            {elemento['email']}
            \t{elemento['telefone']}"""))
    elif opcao ==3:
        for elemento in agenda:
            print(f"""{elemento['nome']}\t")
            {elemento['email']}
            \t{elemento['telefone']}""")
        else:
            print("Não há nenhum nome")

    elif opcao ==4:
        nomebusca = input('Informe o nome para busca:')
        posicao = -1
        for elemento in agenda:
            posicao= posicao +1
            if elemento['nome'].lower() == nomebusca.lower():
                break
            if posicao !=-1:
                agenda[posicao]['nome']=input("Informe o nome: ")
                agenda[posicao]['email']=input("Informe o e-mail: ")
                agenda[posicao]['telefone']=input("Informe o telefone: ")
    elif opcao==5:
        nomebusca = input('Informe o nome para busca:')
        posicao = -1
        for elemento in agenda:
            posicao= posicao +1
            if elemento['nome'].lower() == nomebusca.lower():
                break
            if posicao !=-1:
                agenda.pop(posicao)
    elif opcao ==9:
        break
    
    if opcao.lower() == 'n':
            break
    if posicao != -1:
        agenda.pop(posicao)
            