#importar as bibliotecas
import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf

#chamar pagina
def markowitz():
    start = st.sidebar.date_input('Data de Início', value=pd.datetime(2015, 1, 1))
    end = st.sidebar.date_input('Data Final')
    ticker_1 = st.sidebar.text_input('TICKER - Yahoo Finance', value='EEMV')
    ticker_2 = st.sidebar.text_input('TICKER - Yahoo Finance', value='VSS')
    ticker_3 = st.sidebar.text_input('TICKER - Yahoo Finance', value='IVAL')
    ticker_4 = st.sidebar.text_input('TICKER - Yahoo Finance', value='SLYV')
    ticker_5 = st.sidebar.text_input('TICKER - Yahoo Finance', value='QVAL')
    ticker_6 = st.sidebar.text_input('TICKER - Yahoo Finance', value='SPHQ')
    acoes = [ticker_1, ticker_2, ticker_3, ticker_4, ticker_5]
    dados = yf.download(acoes, start=start, end=end)['Adj Close']
    st.write(dados)
    # checando os dados
    # ------st.write(dados.describe())
    # calculo dos retornos diários e anuais
    retorno_diario = dados.pct_change()
    retorno_anual = retorno_diario.mean() * 250
    # ---------st.write(retorno_diario)
    # cálculo da covariância diária e anual
    cov_diaria = retorno_diario.cov()
    cov_anual = cov_diaria * 250
    # vamos criar 4 listas para armazenar os valores do retorno da carteira, o peso de cada ação, a volatilidade e o sharpe ratio
    # empty lists to store returns, volatility and weights of imiginary portfolios
    retorno_carteira = []
    peso_acoes = []
    volatilidade_carteira = []
    sharpe_ratio = []
    # vamos usar uma simulação aleatória
    numero_acoes = len(acoes)
    numero_carteiras = 100000
    np.random.seed(101)
    # vamos fazer um for loop para preencher as lista que criamos anteriormente
    for cada_carteira in range(numero_carteiras):
        # vamos dar um peso aleatório para cada ação dentro de cada carteira
        peso = np.random.random(numero_acoes)
        peso /= np.sum(peso)
        # vamos calcular o retorno das carteiras
        retorno = np.dot(peso, retorno_anual)
        # vamos calcular a volatilidade das carteiras
        volatilidade = np.sqrt(np.dot(peso.T, np.dot(cov_anual, peso)))
        # vamos calcular o índice de Sharpe de cada carteira
        sharpe = retorno / volatilidade
        # aqui nós usamos o método apend para incluir cada carteira nas listas criadas anteriormente
        sharpe_ratio.append(sharpe)
        retorno_carteira.append(retorno)
        volatilidade_carteira.append(volatilidade)
        peso_acoes.append(peso)
        carteira = {'Retorno': retorno_carteira,
                    'Volatilidade': volatilidade_carteira,
                    'Sharpe Ratio': sharpe_ratio}
    for contar, acao in enumerate(acoes):
        carteira[acao + ' Peso'] = [Peso[contar] for Peso in peso_acoes]
    # vamos transformar nosso dicionário em um dataframe
    df_1 = pd.DataFrame(carteira)
    # vamos nomear as colunas do novo dataframe
    # plt.style.use('seaborn-dark')
    # df_1.plot.scatter(x='Volatilidade', y='Retorno', c='Sharpe Ratio',
    #                cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
    # plt.xlabel('Volatilidade')
    # plt.ylabel('Retorno Esperado')
    # plt.title('Fronteira Eficiente de Markowitz')
    # plt.show()
    # st.pyplot(plt)
    # plotar gráfico
    import plotly.express as px

    fig = px.scatter(df_1, x="Volatilidade", y="Retorno", color='Sharpe Ratio', marginal_x='histogram',
                     marginal_y='histogram')
    st.plotly_chart(fig)

