#baixar as bibliotecas
import streamlit as st
from streamlit_option_menu import option_menu

#importar paginas
import paginas.fronteira_eficiente as fe
import paginas.relatorio_performance as rp
import paginas.inicio as ic
import paginas.prophet as pt
from PIL import Image

#configuracao icone
#colocar outra imagem de icone
img = Image.open('Capa_Home.png')

#configuracao de pagina
#procurar emoji para modificar icone do app page_icon procurara na biblioteca tambem
st.set_page_config(page_title="Smart Portfolio",
                   page_icon='0x1f602:',
                   layout="centered",
                   initial_sidebar_state="expanded",
                   menu_items={'Get help': None,
                               "Report a Bug": None,
                               "About": None
                                }
                   )
#ocultar o menu
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

#paginas
st.sidebar.write('---')
st.sidebar.markdown("<h3 style='text-align: center; color:#F63366; font-size:20px;'><b>Bem Vindo ao Smart Portfolio !<b></h3>",
                unsafe_allow_html=True)
pagina = ['Início', 'Relatório Performance', 'Prophet', 'Fronteira Eficiente']
pagina = st.sidebar.selectbox("Selecione uma funcionalidade:", pagina)

#pagina com navegation bar
pagina = option_menu(
    menu_title= "Menu",
    options=['Início','Relatório Performance', 'Prophet', 'Fronteira Eficiente'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal'
)

if pagina == 'Início':
    ic.inicio()

if pagina == 'Relatório Performance':
    rp.relatorio_performance()

if pagina == 'Prophet':
    pt.prophet()

if pagina == 'Fronteira Eficiente':
    fe.fronteira_eficiente()

#contato
st.sidebar.write('---')
expander = st.sidebar.expander('Contato')
expander.write("Adoraria saber o que você achou !")
expander.write('Fale comigo nas redes sociais:')
expander.write('[LinkedIn](https://www.linkedin.com/in/david-sousa-ab6826198/) ou [Instagram](https://www.instagram.com/davidksousa/)')




