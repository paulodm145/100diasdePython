#IMPRIMI NA TELA SE O NÚMERO É PRIMO
def primo(): #criação da função para verificar 
    primo = int(input("INFORMO UM NÚMERO:_"))
    total = 0
    for i in range(2, primo+1):
        if i != primo:
            i = primo % i
            if i == 0:
                total += 1
                print("Resultado: NÃO É PRIMO - Foi Divisivel"+str(total))
                break
        else:
            print ('Resultado: É PRIMO')
            break
#Com o WHILE TRUE entro em execução até que seja informado
# não pelo Usuário
while True:
    a = input("Executar Aplicativo( s/n ):_")
    if(a == "s"):
        primo()
    else:
        exit(0)