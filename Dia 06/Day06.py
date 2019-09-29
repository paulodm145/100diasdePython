#IMPRIMI NA TELA SE O NÚMERO É PRIMO
def primo(): #criação da função para verificar 
    num = int(input('Digite um Nº:__'))
    total = 0
    for c in range(1, num+1):
        if num % c == 0:
            print('\033[33m', end='')
            total +=1
        else:
            print('\033[31m', end='')
        print('{}'.format(c), end='-')
    print('\n\033[m0 numero {} foi divisivel {} vezes'.format(num , total))
    if total == 2:
        print('POR ISSO ELE É PRIMO!')
    else:
        print('E POR ISSO ELE NÃO É PRIMO')
#Com o WHILE TRUE entro em execução até que seja informado
# não pelo Usuário
while True:
    a = input("Executar Aplicativo( s/n ):_")
    if(a == "s"):
        primo()
    else:
        exit(0)