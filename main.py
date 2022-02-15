#baixar as bibliotecas
import streamlit as st

#importar paginas
import paginas.fronteira_eficiente as fe
import paginas.relatorio_performance as rp
import paginas.inicio as ic
import paginas.prophet as pt

#configuracao de pagina
st.set_page_config(page_title="Smart Portfolio",
                   page_icon=":robot_face:",
                   layout="centered",
                   initial_sidebar_state="expanded",
                   menu_items={'Get help': None,
                               "Report a Bug": None,
                               "About": None
                                }
                   )
#paginas

st.sidebar.markdown("<h3 style='text-align: center; color:black; font-size:20px;'><b>Bem Vindo ao Smart Portfolio !<b></h3>",
                unsafe_allow_html=True)
st.write('.')
pagina = ['Início', 'Relatório Performance', 'Prophet', 'Fronteira Eficiente']
pagina = st.sidebar.selectbox("Selecione uma funcionalidade:", pagina)

if pagina == 'Início':
    ic.inicio()

if pagina == 'Relatório Performance':
    rp.relatorio_performance()

if pagina == 'Prophet':
    pt.prophet()

if pagina == 'Fronteira Eficiente':
    fe.fronteira_eficiente()

#contato
expander = st.sidebar.expander('Contato')
expander.write("Adoraria saber o que você achou !")
expander.write('Fale comigo nas redes sociais:')
expander.write('[LinkedIn](https://www.linkedin.com/in/david-sousa-ab6826198/) ou [Instagram](https://www.instagram.com/davidksousa/)')




