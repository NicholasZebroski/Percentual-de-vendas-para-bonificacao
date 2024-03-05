venda_2022 = float(input('Informe a quantidade de vendas em 2022:'))
venda_2023 = float(input('Informe a quantidade de vendas em 2023:'))

var_percentual = 100 * (venda_2023 - venda_2022) / venda_2022

if var_percentual > 20:
    print('Bonificação para o time de vendas.')
elif 2 <= var_percentual <= 20:
    print('Pequena bonificação para o time de vendas.')
elif -10 <= var_percentual < 2:
    print('Planejamento de políticas de incentivo às vendas.')
else:
    print('Corte de gastos.')

