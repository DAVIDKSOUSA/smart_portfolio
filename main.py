#baixar as bibliotecas
import streamlit as st

#importar paginas
import paginas.fronteira_eficiente as fe
import paginas.relatorio_performance as rp
import paginas.inicio as ic
import paginas.prophet as pt


def p_title(title):
    st.markdown(f'<h3 style="text-align: left; color:#F63366; font-size:28px;">{title}</h3>', unsafe_allow_html=True)


#configuracao de pagina
st.set_page_config(page_title="Condor Portfólio",
                   page_icon=":robot_face:",
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )
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

#contato
expander = st.sidebar.expander('Contact')
expander.write("I'd love your feedback :smiley: Want to collaborate? Develop a project? Find me on [LinkedIn](https://www.linkedin.com/in/lopezyse/), [Twitter](https://twitter.com/lopezyse) and [Medium](https://lopezyse.medium.com/)")




