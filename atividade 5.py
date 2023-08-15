contador = 0
soma=0
print('Sistema para  media de altura [05 pessoas]')
while contador < 5:
    altura =float(input('Digite o valor da altura:'))
    soma = soma + altura
    contador = contador + 1
media = soma / contador
print('A media das altura é de ',media)