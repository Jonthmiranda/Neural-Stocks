# Importando bibliotecas necessárias
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_percentage_error
from sklearn.neural_network import MLPRegressor
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Qual ação deseja conferir?
ticker_simb = input("Qual ação deseja conferir hoje?\n\n")
stock = yf.Ticker(ticker_simb)

# Fazendo o download dos preços no periodo x até o dia de hoje
end_data = datetime.now().strftime('%Y-%m-%d')
data = yf.download(ticker_simb, start='2020-07-30', end=end_data, progress=False)

# Informações que tenho
features = data[['Open', 'High', 'Low', 'Volume']]
# Informações para descobrir
target = data['Adj Close']


# Normalizando os dados, aprende a média e o desvio padrão de cada caracteristica
#???
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Dividindo os dados em treino e teste
x_train, x_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

# Criando e treinando a Rede Neural com MLPRegressor
mlp = MLPRegressor(hidden_layer_sizes=(254, 128), activation='relu', solver='adam', max_iter=500, random_state=42)
mlp.fit(x_train, y_train)

# Fazendo previsões com o x_test
predictions = mlp.predict(x_test)

#transforma os dois em lista
y_test_list = list(y_test)
predictions_list = list(predictions)
print(f"\n\nprevisões: {predictions_list}\n")
print(f"\n valores reais: {y_test_list}\n")


tolerance = 0.02 #2% de tolerancia

# Avaliando o modelo com r2 = 1 - soma dos quadrados dos resíduos (ssr) / Soma total dos quadrados (sst)
#se = 1 os valores previstos estão totalmente alinhados aos observados
#se = 0 indica que não é melhor do que usar a média dos valores observados como predição
#se = negativo o modelo foi pior do que uma linha horizontal representando a média dos valores
r2 = r2_score(y_test_list, predictions_list)
print(f"\nR2 = {r2}\n")

# Avaliando modelo com mape (Erro Percentual Absoluto Médio)
#se 0% indica modelo perfeito, todas previsões são exatas
#se 10% infica erro percentual absoluto entre o valor real e o previsto é 10% (sem tolerancia)
mape = mean_absolute_percentage_error(y_test_list, predictions_list)
print(f"MAPE: {mape * 100}%\n")

#Avaliando modelo com porcentagem de acertos dentro da tolerancia
#se 100% significa que o modelo faz todas as previsões corretamente
#se 0% significa que todas as previsões estavam erradas
correct_predictions = np.abs(predictions - y_test) / y_test <= tolerance
accuracy = np.mean(correct_predictions) * 100
print(f"Porcentagem de acertos (dentro de {tolerance*100}%): {accuracy}%")

#gráfico
# Tamanho do gráfico
plt.figure(figsize=(20, 12))

# Plotando os valores reais
plt.plot(y_test_list, label='Valores Reais', color='blue')

# Plotando os valores previstos
plt.plot(predictions_list, label='Valores Previstos', color='red')

# Adicionando título e rótulos
plt.title('Comparação entre Valores Reais e Previstos')
plt.xlabel('Índice')
plt.ylabel('Valores')

# Adicionando legenda
plt.legend()

# Mostrando o gráfico
plt.show()