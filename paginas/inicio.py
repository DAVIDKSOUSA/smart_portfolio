#importar bibliotecas
import streamlit as st
from streamlit_lottie import st_lottie
import requests

#animacao
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_gdt35llx.json')

#chamar pagina
def inicio():
    #st.image('/Users/davidsousa/Prophet/Capa Home.png', use_column_width='always')
    st.title('Análise de um Portifólio de Investimentos')
    st.subheader('Como analisar minha carteira de investimento ?')
    st.write(
        'O processo de alocação patrimonial, apesar de ser simples não é fácil.'
        'Devido à quantidade exarcebada de informações que temos, através dos '
        'meios de comunicação, o investidor fica confuso em relação à composição'
        'da sua carteira, tanto em relação à quantidade quanto em relação a classe de ativo. '
        'Nesse contexto esse aplicativo foi concebido com a intenção de auxiliar o processo de alocação.'
        'O aplicativo não irá te mostrar em qual classe de ativo investir, contudo uma vez definida a classe de ativo'
        'é possível identificar a alocação mais eficaz, onde pode-se observar uma maior retorno esperado para um menor'
        'risco (volatilidade).'
        )

    st.write(
        '[Saiba Mais](https://www.webfx.com/tools/emoji-cheat-sheet/)')  # colocar link blog mudar o nome saiba mais
    with st.container():
        st.write('---')
        left_column, right_column = st.columns(2)
        with left_column:
            st.header('Me siga nas mídias sociais para saber mais sobre alocação patrimonial.')
            st.write('##')
            st.write(
                '''
                Link Mídias Sociais
                - @davidksousa
                - linkdin
                
                '''
            )
            st.write('[Canal do YouTube](https://www.youtube.com/watch?v=61HE1kdavXk&list=RD61HE1kdavXk&start_radio=1)')
        with right_column:
            st_lottie(lottie_coding, height=400, key='coding')

