qtdmaca = int(input('quantidade de maçã: '))
if qtdmaca >=12:
  qtdmaca = 1.0 * qtdmaca
  print('valor paga R$',qtdmaca, 'valor paga')
else:
  qtdmaca= 1.30 * qtdmaca
  print('O valor da compra foi de : ', qtdmaca)
