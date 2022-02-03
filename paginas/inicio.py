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
    st.image('/Users/davidsousa/Prophet/Capa Home.png', use_column_width='always')
    st.title('Análise de um Portifólio de Investimentos')
    st.subheader('Como analisar minha carteira de investimento ?')
    st.write(
        'O processo de alocação patrimonial, apesar de ser simples não é fácil.'
        'Devido à quantidade exarcebada de informações que temos através dos meios de comunicação, muitas vezes o'
        'investidor fica confuso em relação à composição da sua carteira. Tanto em relação à quantidade quanto em'
        'relação a classe de ativo. Nesse contexto esse aplicatico foi concebido com a intenção de auxiliar o    '
        'no processo de alocação.'
        ''
        'o último grau de sofisticaçao é a simplicidade.'
        )
    st.write(
        '[Saiba Mais](https://www.webfx.com/tools/emoji-cheat-sheet/)')  # colocar link blog mudar o nome saiba mais
    with st.container():
        st.write('---')
        left_column, right_column = st.columns(2)
        with left_column:
            st.header('What I do')
            st.write('##')
            st.write(
                '''
                dsavdvsfvasfv
                - asdfasdf
                - asdfasdvas
                asdvasdv
                kjshajksfhkls
                '''
            )
            st.write('[Canal do YouTube](https://www.youtube.com/watch?v=61HE1kdavXk&list=RD61HE1kdavXk&start_radio=1)')
        with right_column:
            st_lottie(lottie_coding, height=400, key='coding')

