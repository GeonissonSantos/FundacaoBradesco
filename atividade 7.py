numero=0
maior=0
menor=9999
media=0
contador=0
soma=0
numero= int(input('Digite o numero desejado'))
while numero > 0:
    if numero < menor:
     menor = numero
    elif numero > maior:
        maior = numero
    soma= soma + numero
    contador=contador+1
    numero=int(input('Digite o numero desejado'))
media = soma/contador
print(maior)
print(menor)
print(media)
