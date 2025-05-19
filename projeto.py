import time

#Declaração Variaveis
opcao = ""
alunos = {}

#Funções
def exibeLista():
    
    if  len(alunos) == 0:
        print("Não há nenhum aluno cadastrado!")
    else:
        for codigo, nome in alunos.items():
            print(f"{codigo}. {nome}")


#Menu principal
while True:
    print("########################\nBem vindo a Renstudents!\n\nSelecione uma das opções")

    print("\n1. Sou professor")
    print("2. Sou aluno")
    print("0. Encerrar programa")


    while True:
        try:
            opcaoPrin = int(input("Digite o número: ")) #Opção principal
            if opcaoPrin < 0 or opcaoPrin >= 3:
                raise ValueError
            break
        except ValueError:
            print("\nEntrada inválida! Digite um número inteiro que está na lista. ")
            print("1. Sou professor")
            print("2. Sou aluno")
            print("0. Encerrar programa")

    #SEÇÃO PROFESSOR
    if opcaoPrin == 1:
        while True:
            print("\n\n###############\nSelecione uma das opções")

            print("1. Consultar alunos")
            print("2. Cadastrar aluno")
            print("3. Remover aluno")
            print("4. Alterar aluno")
            print("5. Calcular nota")

            print("0. Sair para o menu principal")

            #Validação de entrada
            while True:
                try:
                    opcao = int(input("Digite a opção: "))
                    if opcao >= 6 or opcao < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("\n1. Consultar alunos")
                    print("2. Cadastrar aluno")
                    print("3. Remover aluno")
                    print("4. Alterar aluno")
                    print("5. Calcular nota")
                    print("0. Sair para o menu principal")
                    print("\nEntrada inválida! Digite um número inteiro que está na lista")

            #EXIBIR LISTA
            if opcao == 1:
                print("########################\nConfira a lista dos alunos")
                exibeLista()
                input("\nPressione Enter para retornar ao menu")
            
            #CADASTRAR ALUNO
            elif opcao == 2:

                #Declarando as variáveis
                novo = 0
                decisao = 1

                #Código irá se repetir enquanto a decisão do input da linha 111 for '1'
                while decisao == 1:
                    if len(alunos) == 0:
                        cod = 1
                    else: 
                        cod = max(alunos)
                        cod += 1
                    
                    print("########################\nCadastrar novo aluno\n")
                    

                    #Validação de entrada
                    while novo != "0":
                        try:
                            novo = input("Digite o nome do aluno (ou digite 0 para retornar ao Menu): ")
                            if novo == "":
                                raise ValueError
                            break
                        except ValueError:
                            print("Entrada inválida! Digite algo")

                    #Retornar ao Menu        
                    if novo == "0":
                        break

                    else:
                        alunos[cod] = novo
                        print(f"'{novo}' foi adicionado com sucesso!")
                        time.sleep(1)
                        while True:   
                            try: 
                                decisao = int(input("\nDeseja cadastrar outro aluno? \n(Digite 1 para SIM / 2 para NÃO): "))
                                if decisao < 1 or decisao>2:
                                    raise ValueError
                                break
                            except ValueError:
                                print("Entrada invalida! Digite um valor entre 1 e 2")
                        
            
            #EXCLUIR ALUNO
            elif opcao == 3:
                print("\n########################\nLista de alunos")
                exibeLista()
                if len(alunos) == 0:
                    input("Digite Enter para retornar ao Menu")
                    continue
                
                chave = ""
                while chave is not 0:

                    #Validação de entrada
                    while True:
                        try:
                            chave = int(input("\nDigite o código do aluno a ser removido (Para sair, digite '0'): "))
                            break
                        except ValueError:
                            print("\nEntrada inválida! Por favor, digite um número inteiro. ")


                    if chave == 0:
                        break
                    while chave not in alunos:
                        chave = int(input(f"Código {chave} não foi encontrado!\nTente novamente outro número ou digite '0' para sair: "))
                        if chave == 0:
                            break 
                        
                    if chave == 0:
                        break   
                    removido = alunos.pop(chave)
                    print(f"Aluno(a) {removido} foi removido com sucesso!")
                    time.sleep(2)
                    break          
        
            
            #ALTERAR ALUNO
            elif opcao == 4:
                #Declarando variaveis
                codAlterar = ""
                nomeAlterar = ""

                print("##############\nALTERAR ALUNO\n")
                exibeLista()

                if len(alunos) == 0:
                    input("Aperte Enter para retornar ao menu")
                else:

                    #Validação de entrada do código
                    while codAlterar != 0:
                        try:
                            codAlterar = int(input("Digite o código do aluno a ser alterado (ou digite '0' para retornar ao Menu): "))
                        
                            if codAlterar < 0:
                                raise ValueError
                            
                            elif codAlterar not in alunos:
                                raise ValueError
                            
                            break
                        except ValueError:
                            print("")
                            exibeLista()
                            print("Entrada inválida! Digite um número inteiro que esteja na lista")
                    if codAlterar == 0:
                        continue
                    else:

                        #Validação entrada do nome
                        while nomeAlterar != "0":
                            try:
                                nomeAlterar = input("Digite o novo nome (ou digite '0' para retornar ao Menu): ")
                                if nomeAlterar == "":
                                    raise ValueError
                                break
                            except ValueError:
                                print("Entrada inválida! Digite algo.")
                        if nomeAlterar == "0":
                            continue

                        
                        else:
                            nomeAnterior = alunos[codAlterar]
                            alunos[codAlterar] = nomeAlterar
                            print(f"\nNome do aluno '{nomeAnterior}' alterado para '{alunos[codAlterar]}'")
                            input("Aperte Enter para retornar ao Menu")
                                                
                
            elif opcao == 5:
                print("\nCalcular notas")
                nota = ""
                notas = []

                for i in range(4):
                    while True:
                        try:

                            nota = float(input(f"informe a primeira nota ({i+1}/4): "))
                            break
                        except ValueError:
                            print("Digite um valor inteiro!")

                    notas.append(nota)

                media = sum(notas) / len(notas)
                print(f"A média é de {media}")
                input("\nDigite Enter para retornar ao Menu")   

            #RETORNA AO MENU PRINCIPAL
            elif opcao == 0:
                break

    #SEÇÃO ALUNO
    elif opcaoPrin == 2:
        while True:
            #Declarando Variáveis
            opcaoAluno = ""

            print("\n###################################################\nBEM VINDO A REINSTUDENTS! SELECIONE UMA DAS OPÇÕES\n")
            
            print("1. Boas práticas de Segurança Digital")
            print("2. LGPD")
            print("3. Ética, Cidadania e Sustentabilidade")
            print("0. Sair para o menu principal")

            while True:
                try:
                    opcaoAluno = int(input("Digite a opção: "))
                    if opcaoAluno >= 4 or opcaoAluno < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("\n\n1. Boas práticas de Segurança Digital")
                    print("2. LGPD")
                    print("3. Ética, Cidadania e Sustentabilidade")
                    print("0. Sair para o menu principal")
                    print("\nEntrada inválida! Digite um número inteiro que está na lista")


            #Boas Práticas de Segurança Digital
            if opcaoAluno == 1:
                while True:

                    #Declarando variáveis
                    opc1 = ""

                    print("\n\n############################################################\nBem vindo às Aulas sobre Boas práticas de Segurança Digital")

                    print("\n1. Segurança em redes públicas e uso de VPN")
                    print("2. Autenticação em dois fatores (2FA) e proteção de contas")
                    print("3. Monitoramento de atividades e resposta a incidentes")
                    print("0. Sair para selecionar outra aula")
                    
                    while True:
                        try:
                            opc1 = int(input("Digite o número: "))
                            if opc1 < 0 or opc1 >= 4:
                                raise ValueError
                            break
                        except ValueError:
                            print("\n\n1. Segurança em redes públicas e uso de VPN")
                            print("2. Autenticação em dois fatores (2FA) e proteção de contas")
                            print("3. Monitoramento de atividades e resposta a incidentes")
                            print("0. Sair para selecionar outra aula")
                            print("\nEntrada inválida! Digite um número inteiro que está na lista")
                    #Aula 1
                    if opc1 == 1:
                        print("\n\nSegurança em redes públicas e uso de VPN🧠")
                        print("\nQuando estamos fora de casa e precisamos acessar a internet, é comum usar redes Wi-Fi públicas, como em cafés, bibliotecas ou aeroportos. "
                                "\nNo entanto, essas redes são extremamente vulneráveis. Qualquer pessoa conectada à mesma rede pode, com pouco conhecimento técnico, interceptar seus dados. "
                                "\nIsso inclui senhas, mensagens e até dados bancários.\n\n"
                                "Para se proteger, evite acessar contas importantes em redes abertas. Se for inevitável, utilize uma VPN (Rede Virtual Privada). "
                                "\nA VPN cria um túnel criptografado entre seu dispositivo e a internet, tornando muito mais difícil para qualquer pessoa espiar sua conexão. "
                                "\nExistem VPNs gratuitas e pagas, mas prefira as que têm boa reputação e política clara de privacidade.\n\n"
                                "📌 Dica prática: Nunca realize operações bancárias, compras online ou troque senhas em redes Wi-Fi públicas sem usar uma VPN confiável.\n")
                        input("Digite enter para retornar. ")

                    #Aula 2
                    elif opc1 == 2:
                        print("\n\nAutenticação em dois fatores (2FA) e proteção de contas🧠")
                        print("\nMesmo com uma boa senha, sua conta pode estar em risco. Vazamentos de dados e ataques de força bruta são comuns. "
                        "\nPor isso, ativar a autenticação em dois fatores (2FA) é uma medida altamente recomendada para proteger suas contas.\n\n"
                        "A 2FA exige um segundo código para login, além da senha. Esse código pode ser enviado por SMS, e-mail, ou gerado por aplicativos como Google Authenticator ou Authy. "
                        "\nDessa forma, mesmo que alguém descubra sua senha, não conseguirá acessar sua conta sem esse segundo fator.\n\n"
                        "📌 Dica prática: Ative a 2FA em todos os serviços que oferecem essa opção, especialmente e-mails, redes sociais e contas bancárias. "
                        "Isso reduz drasticamente o risco de invasão.\n")
                        input("Digite enter para retornar. ")

                    #Aula 3
                    elif opc1 == 3:
                        print("\n\nMonitoramento de atividades e resposta a incidentes🧠")
                        print("A segurança digital não termina na prevenção — ela também envolve monitorar suas contas e saber\ncomo reagir rapidamente a possíveis incidentes. "
                        "\nMuitos serviços oferecem notificações de login, alertas de atividade suspeita e \nrelatórios de dispositivos conectados. Preste atenção a esses sinais.\n\n"
                        "Verifique com frequência:\n"
                        "- Onde e quando sua conta foi acessada.\n"
                        "- Quais dispositivos estão conectados.\n"
                        "- Se houve tentativas de login com falha ou mudanças de senha.\n\n"
                        "Caso identifique algo estranho, mude sua senha imediatamente e revise as configurações de segurança da conta. "
                        "\nEm alguns casos, é recomendável revogar sessões ativas e até entrar em contato com o suporte da plataforma.\n\n"
                        "📌 Dica prática: Use o hábito de revisar sua “segurança de conta” uma vez por mês, \nassim como você revisa seu extrato bancário.\n")
                        input("Digite enter para retornar. ")

                    elif opc1 == 0:
                        break
                    
            #LGPD
            elif opcaoAluno == 2:
                while True:

                    #Declarando variáveis
                    opc2 = ""

                    print("\n\n#############################################\nBem vindo às Aulas sobre LGPD")

                    print("\n1. O que é a LGPD e por que ela é importante")
                    print("2. Dados pessoais e sensíveis – entenda a diferença")
                    print("3. Direitos dos titulares e boas práticas de conformidade")
                    print("0. Sair para selecionar outra aula")
                    
                    while True:
                        try:
                            opc2 = int(input("Digite o número: "))
                            if opc2 < 0 or opc2 >= 4:
                                raise ValueError
                            break
                        except ValueError:
                            print("\n\n1. O que é a LGPD e por que ela é importante")
                            print("2. Dados pessoais e sensíveis – entenda a diferença")
                            print("3. Direitos dos titulares e boas práticas de conformidade")
                            print("0. Sair para selecionar outra aula")
                            print("\nEntrada inválida! Digite um número inteiro que está na lista")

                    if opc2 == 1:
                        print("\n\nO que é a LGPD e por que ela é importante🧠")
                        print("\nA LGPD (Lei Geral de Proteção de Dados), em vigor no Brasil desde 2020, \ntem como objetivo garantir o direito à privacidade e à proteção dos dados pessoais dos cidadãos. "
                        "\nEla se aplica a qualquer organização, pública ou privada, que coleta, armazena ou trata \ndados de pessoas físicas no Brasil, mesmo que esteja localizada fora do país.\n\n"
                        "\nA lei estabelece regras claras sobre como os dados devem ser coletados, tratados e \narmazenados, e obriga as empresas a adotarem medidas de segurança para proteger essas informações. "
                        "\nAlém disso, reforça o direito dos titulares sobre seus próprios dados, permitindo \nque solicitem correções, exclusão ou acesso às informações que estão sendo processadas.\n\n"
                        "📌 Dica prática: Se você trabalha em uma empresa que coleta dados de clientes, \ncertifique-se de que há consentimento claro e documentado para isso.\n")
                        input("Digite enter para retornar. ")
                    elif opc2 == 2:
                        print("\n\nDados pessoais e sensíveis – entenda a diferença🧠")
                        print("\nA LGPD define dois tipos principais de dados: pessoais e sensíveis. "
                        "\nDados pessoais são aqueles que permitem identificar uma pessoa direta ou indiretamente, como nome, CPF, e-mail, endereço ou número de telefone. "
                        "\nJá os dados sensíveis são mais delicados, pois envolvem informações como origem racial, convicções religiosas, opinião política, saúde, vida sexual ou dados biométricos.\n\n"
                        "\nO tratamento de dados sensíveis exige cuidados ainda maiores e, geralmente, requer consentimento explícito e por escrito do titular. "
                        "\nO uso indevido desses dados pode acarretar penalidades severas, além de danos à imagem da empresa.\n\n"
                        "📌 Dica prática: Nunca colete dados sensíveis sem uma justificativa legal clara e sem informar o titular exatamente como essas informações serão usadas.\n")
                        input("Digite enter para retornar. ")
                    elif opc2 == 3:
                        print("\n\nDireitos dos titulares e boas práticas de conformidade🧠")
                        print("\nA LGPD garante aos titulares de dados diversos direitos, como o de acessar suas informações, solicitar correções, revogar consentimentos ou até pedir a exclusão dos dados. "
                        "\nAs empresas são obrigadas a responder a essas solicitações dentro de prazos estabelecidos.\n\n"
                        "Para estar em conformidade com a LGPD, as organizações devem adotar medidas como o mapeamento dos dados pessoais tratados, controle de acesso, registro de consentimento e capacitação da equipe. "
                        "\nAlém disso, devem nomear um encarregado pelo tratamento de dados (o DPO – Data Protection Officer), responsável por atender os titulares e fiscalizar o cumprimento da lei.\n\n"
                        "📌 Dica prática: Mantenha políticas de privacidade claras e acessíveis, e treine seus colaboradores sobre boas práticas no uso e proteção de dados pessoais.\n")
                        input("Digite enter para retornar. ")
                    elif opc2 == 0:
                        break

            #ÉTICA, CIDADANIA E SUSTENTABILIDADE
            elif opcaoAluno == 3:
                while True:    

                    #Declarando variáveis
                    opc3 = ""

                    print("\n\n#############################################\nBem vindo às Aulas sobre Ética, Cidadania e Sustentabilidade")

                    print("\n1. Ética no uso da tecnologia e responsabilidade profissional")
                    print("2. Cidadania digital: comportamento consciente e seguro online")
                    print("3. Sustentabilidade na TI: boas práticas ambientais e sociais")
                    print("0. Sair para selecionar outra aula")
                    
                    while True:
                        try:
                            opc3 = int(input("Digite o número: "))
                            if opc3 < 0 or opc3 >= 4:
                                raise ValueError
                            break
                        except ValueError:
                            print("\n1. Ética no uso da tecnologia e responsabilidade profissional")
                            print("2. Cidadania digital: comportamento consciente e seguro online")
                            print("3. Sustentabilidade na TI: boas práticas ambientais e sociais")
                            print("0. Sair para selecionar outra aula")
                            print("\nEntrada inválida! Digite um número inteiro que está na lista")

                    #Aula 1
                    if opc3 == 1:
                        print("\n\nÉtica no uso da tecnologia e responsabilidade profissional 🧠")
                        print("\nTrabalhar com tecnologia não envolve apenas habilidades técnicas — também exige responsabilidade ética. "
                        "\nProfissionais de TI têm acesso a informações sensíveis, tomam decisões com grande impacto e muitas vezes "
                        "\nestão por trás de sistemas que afetam milhares de pessoas.\n\n"
                        "\nÉtica na TI significa agir com integridade, respeitar a privacidade dos usuários, evitar o uso indevido de dados "
                        "\ne não se beneficiar de falhas ou brechas em sistemas. Manipular resultados, invadir contas ou espalhar software ilegal "
                        "são atitudes antiéticas que comprometem a confiança no setor.\n\n"
                        "📌 Dica prática: Sempre se pergunte: “Se todos soubessem que eu fiz isso, ainda pareceria certo?” "
                        "\nssa reflexão ajuda a manter a ética no centro das suas ações.\n")
                        input("Digite Enter para retornar. ")  

                    #Aula 2
                    elif opc3 == 2:
                        print("\n\nCidadania digital: comportamento consciente e seguro online 🧠")
                        print("\nCidadania digital vai além de saber usar redes sociais ou e-mail. Trata-se de agir com respeito, empatia e "
                        "\nresponsabilidade no mundo virtual. Isso inclui combater fake news, respeitar os direitos autorais, evitar discursos de ódio "
                        "\ne manter a segurança online.\n\n"
                        "No campo da tecnologia, ser um cidadão digital exemplar também significa promover a inclusão, garantir acessibilidade nas "
                        "\nferramentas que você desenvolve e orientar outras pessoas sobre boas práticas.\n\n"
                        "📌 Dica prática: Antes de compartilhar algo na internet, verifique a fonte e pense no \nimpacto que aquela informação pode causar. "
                        "\nE lembre-se: atrás de cada perfil, existe uma pessoa real.\n")
                        input("Digite Enter para retornar. ")  

                    #Aula 3
                    elif opc3 == 3:
                        print("\n\nSustentabilidade na TI: boas práticas ambientais e sociais 🧠")
                        print("\nA área de TI também tem responsabilidade ambiental e social. O uso de energia, o descarte de equipamentos eletrônicos "
                        "\ne o ciclo de vida de softwares e hardwares impactam diretamente o planeta.\n\n"
                        "Boas práticas incluem o uso eficiente da energia, o reaproveitamento ou descarte adequado de equipamentos, a escolha de "
                        "\nfornecedores sustentáveis e o desenvolvimento de soluções que ajudem pessoas e comunidades. Sustentabilidade também passa "
                        "\npela inclusão e pela equidade no acesso à tecnologia.\n\n"
                        "📌 Dica prática: Descarte eletrônicos em pontos de coleta apropriados, use o modo escuro para economizar energia "
                        "\ne dê preferência a equipamentos com selo de eficiência energética.\n")
                        input("Digite Enter para retornar. ")  

                    elif opc3 == 0:
                        break

            #Retornar ao menu principal
            elif opcaoAluno == 0:
                break

    #ENCERRAR PROGRAMA
    elif opcaoPrin == 0:
        break

    else:
        opcaoPrin = input("Opção inválida! Selecione entre a opção 1, 2 e 0")


