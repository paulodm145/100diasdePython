#Estudo Sobre data e Hora
from datetime import date #Módulo datetime importando a clase date

data_atual = date.today()
print(data_atual)           # 2019-07-14
data_atual_br = '0{}/0{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
print(data_atual_br)        #Não é funcional EX: 010/010/2019 - Resolve-se com strftime()
data_ok = data_atual.strftime('%d/%m/%Y') #Agora com a data em String fica mais facil formatar
print(data_ok)
