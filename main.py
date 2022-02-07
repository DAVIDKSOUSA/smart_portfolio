#baixar as bibliotecas
import streamlit as st

#importar paginas
import paginas.fronteira_eficiente as fe
import paginas.relatorio_performance as rp
import paginas.inicio as ic
import paginas.prophet as pt
import paginas.teste_fronteira_eficiente as etf

#configuracao de pagina
st.set_page_config(page_title='Condor Portfólio', page_icon=':dollar:', layout='wide')

#paginas
st.sidebar.title('Escolha a página que deseja acessar.')
pagina = ['Início', 'Relatório Performance', 'Prophet', 'Fronteira Eficiente', 'Teste Fronteira Eficiente']
pagina = st.sidebar.selectbox("Selecione a página que você deseja", pagina)

if pagina == 'Início':
    ic.inicio()

if pagina == 'Relatório Performance':
    rp.relatorio_performance()

if pagina == 'Prophet':
    pt.prophet()

if pagina == 'Fronteira Eficiente':
    fe.markowitz()

if pagina == 'Teste Fronteira Eficiente':
    etf.teste_fronteira_eficiente()



