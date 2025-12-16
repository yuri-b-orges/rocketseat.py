import random

def jogo_adivinhacao():
    print("=" * 50)
    print("JOGO DE ADIVINHAÇÃO")
    print("=" * 50)
    print("\nO computador escolherá um número entre 1 e 100.")
    print("Tente adivinhar qual é esse número!")
    print("A cada palpite, direi se o número correto é MAIOR ou MENOR.")
    print("-" * 50)
    
    # Inicialização do jogo
    input("Pressione ENTER para começar...")
    
    # Gerar número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    palpite = 0
    
    print("\n" + "=" * 50)
    print("O número secreto foi gerado. Boa sorte!")
    print("=" * 50)
    
    # Loop principal do jogo
    while palpite != numero_secreto:
        try:
            # Solicitar palpite do jogador
            palpite = int(input(f"\nTentativa #{tentativas + 1}: Digite seu palpite (1-100): "))
            
            # Validar entrada
            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue
                
            tentativas += 1
            
            # Verificar palpite
            if palpite < numero_secreto:
                print(f"O número secreto é MAIOR que {palpite}.")
            elif palpite > numero_secreto:
                print(f"O número secreto é MENOR que {palpite}.")
            else:
                print("\n" + "=" * 50)
                print(f"PARABÉNS! Você acertou em {tentativas} tentativa(s)!")
                print(f"O número secreto era realmente {numero_secreto}!")
                print("=" * 50)
                
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")
    
    # Perguntar se quer jogar novamente
    while True:
        jogar_novamente = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
        if jogar_novamente in ['S', 'SIM']:
            print("\n" * 3)  # Limpar a tela (parcialmente)
            jogo_adivinhacao()
            return
        elif jogar_novamente in ['N', 'NÃO', 'NAO']:
            print("\nObrigado por jogar! Até a próxima!")
            break
        else:
            print("Por favor, responda com 'S' para sim ou 'N' para não.")

# Versão alternativa mais simples (sem recursão)
def jogo_adivinhacao_simples():
    while True:
        print("\n" + "=" * 50)
        print("JOGO DE ADIVINHAÇÃO - Versão Simples")
        print("=" * 50)
        
        numero_secreto = random.randint(1, 100)
        tentativas = 0
        
        print("\nO computador escolheu um número entre 1 e 100.")
        print("Tente adivinhar! Digite 0 para sair.")
        
        while True:
            try:
                palpite = int(input(f"\nTentativa #{tentativas + 1}: Seu palpite: "))
                
                if palpite == 0:
                    print("Saindo do jogo...")
                    return
                
                if palpite < 1 or palpite > 100:
                    print("Por favor, digite um número entre 1 e 100.")
                    continue
                
                tentativas += 1
                
                if palpite < numero_secreto:
                    print(f"O número secreto é MAIOR que {palpite}.")
                elif palpite > numero_secreto:
                    print(f"O número secreto é MENOR que {palpite}.")
                else:
                    print("\n" + "*" * 50)
                    print(f"🎉 PARABÉNS! Você acertou em {tentativas} tentativa(s)!")
                    print(f"O número era {numero_secreto}!")
                    print("*" * 50)
                    
                    # Mostrar desempenho
                    if tentativas <= 5:
                        print("Excelente! Você é muito bom nisso!")
                    elif tentativas <= 10:
                        print("Bom trabalho!")
                    else:
                        print("Continue praticando!")
                    
                    break
                    
            except ValueError:
                print("Entrada inválida! Digite um número.")
        
        # Perguntar se quer jogar novamente
        novamente = input("\nJogar novamente? (S/N): ").strip().upper()
        if novamente not in ['S', 'SIM']:
            print("\nObrigado por jogar! Até logo!")
            break

# Menu principal
if __name__ == "__main__":
    print("PROGRAMA PROTÓTIPO DE ADIVINHAÇÃO")
    print("\nEscolha uma versão para jogar:")
    print("1. Versão Padrão (com mais detalhes)")
    print("2. Versão Simples (mais direta)")
    print("3. Sair")
    
    while True:
        escolha = input("\nDigite sua escolha (1-3): ").strip()
        
        if escolha == "1":
            jogo_adivinhacao()
            break
        elif escolha == "2":
            jogo_adivinhacao_simples()
            break
        elif escolha == "3":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")