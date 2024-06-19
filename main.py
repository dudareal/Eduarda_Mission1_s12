from conversor_medidas import ConversorMedidas
from conversor_temperatur import Temperatura

print('''
[1]. Metros para Centímetros
[2]. Centímetros para Metros
[3]. Celsius para Fahrenheint
[4]. Fahrenheit para Celsius
''')

opcao = input('Escolha uma opção: ')
valor = float(input('Insira um valor: '))

if opcao == '1':
    resultado = ConversorMedidas.metrosParaCentimetros(valor)
elif opcao == '2':
    resultado = ConversorMedidas.centimetrosParaMetros(valor)
elif opcao == '3':
    resultado = Temperatura.celsiusParaFahrenheint(valor)
else:
    resultado = Temperatura.fahrenheitParaCelsius(valor)
    
print('Resultado:', resultado)