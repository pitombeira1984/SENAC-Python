def saudacao():
    """Coleta o nome e a idade do usuário e imprime uma saudação."""
    try:
        nome = str(input('Digite seu nome: '))
        idade = int(input('Digite sua idade: '))
    except ValueError:
        print("Entrada inválida para a idade. Usando 'idade desconhecida'.")
        idade = 'idade desconhecida'
        
    print(f'Olá, {nome}! Seja bem-vindo(a)! Você tem {idade} anos.')

# Chamada da função. Não é necessário passar argumentos.
saudacao()
