#baixar as bibliotecas
import streamlit as st

#importar paginas
import paginas.fronteira_eficiente as fe
import paginas.relatorio_performance as rp
import paginas.inicio as ic
import paginas.prophet as pt

#configuracao de pagina
st.set_page_config(page_title='Condor Portfólio', page_icon=':dollar:', layout='wide')

#paginas
st.sidebar.title('SELECIONE UMA OPÇÃO')
pagina = ['Início', 'Relatório Performance', 'Prophet', 'Fronteira Eficiente']
pagina = st.sidebar.selectbox("Relatório de perfomance:"
                              "qwefqwef"
                              "qwefwqf", pagina)

if pagina == 'Início':
    ic.inicio()

if pagina == 'Relatório Performance':
    rp.relatorio_performance()

if pagina == 'Prophet':
    pt.prophet()

if pagina == 'Fronteira Eficiente':
    fe.fronteira_eficiente()



