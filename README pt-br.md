Português | [English]()

# Neural-Stocks 1.1

## Descrição

Estudo de um sistema de análise de dados históricos de ações com previsões usando rede neural.

bibliotecas: yfinance, sklearn, numpy e matplot.

## Funcionalidades Principais

- Download dos dados históricos da ação escolhida pelo periodo x até o dia de hoje.


- Análise dos dados e previsão de preço de ações usando rede neural.


- Comparação dos dados com gráficos.


## Requisitos

- Python instalado
- Bibliotecas sklearn , numpy, yfinance, matplot
- Acesso à internet

## Instalação

```bash
git clone https://github.com/Jonthmiranda/Neural-Stocks
```

## Uso

Inicie financas.py usando uma IDE Python ou CMD;

Você deve digitar o código da ação desejada, Ex: apple - AAPL, Nvidia - NVDA etc...

Depois de você escolher o código irá buscar o histórico de valores no Yahoo Finanças, ajustar os dados, análisar os dados e repassar os resultados obtidos, cálculos e gráfico.

## Resultados obtidos

- Foi usado para testes a AAPL (Apple), MSFT (Microsoft), NU (Nubank) e NVDA (Nvidia);
- Foi levado em conta 2% de tolerancia a erros para os resultados 

- APPLE
Durante o desenvolvimento foi usado a AAPL para testes, isso quer dizer as ações da apple foram avaliadas mais vezes pela rede neural, e é claro, resultados mais precisos

Valores reais: 169.35, 143.11, 164.13...

Valores previstos: 168.55, 141.63, 163.32...

R2: 0.99 (R2 vai de 0 á 1, pode dar valor negativo, quando o resultado é 1, indica modelo perfeito)

MAPE: 0.73 (MAPE vai de 0 á 100, quanto mais perto do 0, mais correto está o modelo)

Porcentagem de acerto dentro de 2% de tolerancia: 96.01% (de 0% á 100%, quanto mais proximo ao 100%, mais identicos estão os valores reais e os valores previstos

- Microsoft:
Microsoft foi mostrado algumas vezes para o modelo

R2: 0.99

MAPE: 0.78

Porcentagem: 94.52%

- Nubank
Nubank foi mostrado para o modelo somente esta vez

R2: 0.99

MAPE: 1.51

Porcentagem: 78.19%

- Nvidia
Nvidia nunca foi mostrado e foi usado um período maior do histórico de valores

R2: 0.99

MAPE: 1.95

Porcentagem: 58.70%

## Melhorias

1.1-> Adicionado mais cálculos e gráfico.
