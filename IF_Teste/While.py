while True:
    print("Digite seu nome:")
    name = input()
    
    if name != 'Luiz':
        print("Nome incorreto! Tente novamente.")
        continue
    
    for _ in range(3):  # Dá 3 tentativas de senha
        print("Olá Luiz! Digite sua senha:")
        password = input()
        if password == '1234':
            print("Obrigado!")
            break
        else:
            print("Senha incorreta. Tente novamente.")
    else:
        print("Muitas tentativas incorretas. Tente mais tarde.")
        break
    break