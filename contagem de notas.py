print(f'Programa de conferência de dinheiro')
Valor_final=float(input("Digite o valor final:"))
print(f'{Valor_final:.2f}')
Notas_de_200=float(input("Quantidade de cédulas de 200,00:"))
Notas_de_100=float(input("Quantidade de cédulas de 100,00:"))
Notas_de_50=float(input("Quantidade de cédulas de 50,00:"))
Notas_de_20=float(input("Quantidade de cédulas de 20,00:"))
Notas_de_10=float(input("Quantidade de cédulas de 10,00:"))
Notas_de_5=float(input("Quantidade de cédulas de 5,00:"))
Notas_de_2=float(input("Quantidade de cédulas de 2,00:"))
Valor_total_200=200*Notas_de_200
Valor_total_100=100*Notas_de_100
Valor_total_50=50*Notas_de_50
Valor_total_20=20*Notas_de_20
Valor_total_10=10*Notas_de_10
Valor_total_5=5*Notas_de_5
Valor_total_2=2*Notas_de_2
Soma_total=(Valor_total_2+Valor_total_5+Valor_total_10+Valor_total_20+Valor_total_50+Valor_total_100+Valor_total_200)
Diferença=Valor_final-Soma_total 
if Soma_total - Valor_final == 0 :
    print("O valor está correto")
else : print(f'A diferença é de {Diferença:.2f} reais')


