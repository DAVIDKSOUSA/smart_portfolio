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
    st.markdown("<h3 style='text-align: center; color:red; font-size:40px;'><b>SMART PORTFOLIO<b></h3>",
                unsafe_allow_html=True)
    st.text('')
    st.markdown("<h3 style='text-align: center; color:grey; font-size:20px;'><b>Faça uma análise completa da sua "
                "carteira de investimentos de forma SIMPLES, OBJETIVA e RÁPIDA!<b></h3>",
                unsafe_allow_html=True)
    st.text('')
    st.write(
        'O processo de alocação patrimonial, apesar de ser simples não é fácil. Devido à quantidade exarcebada de infor'
        'mações que temos o investidor fica confuso em relação à composição da sua '
        'carteira, tanto em relação à quantidade quanto a classe de ativo. Nesse contexto esse aplicativo '
        'foi concebido com a intenção de auxiliar nesse processo de alocação. O aplicativo não irá te mostrar em qual class'
        'e de ativo investir, contudo uma vez definida a classe de ativo é possível identificar a alocação eficiente, '
        'onde pode-se observar uma maior retorno esperado para um menor risco (volatilidade).'
        )
    st.write('---')
    st.write(':point_left: Use o menu ao lado e selecione uma tarefa.')
    st.write('---')
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            def p_title(title):
                st.markdown(f'<h3 style="text-align: left; color:#F63366; font-size:28px;">{title}</h3>',
                            unsafe_allow_html=True)
            st.text('')
            p_title('Qual objetivo deste aplicativo ?')
            st.text('')
            st.write(
                'Realizar a analise de ativos financeiros e o comportamento de um portifólio de investimentos através de '
                'análise de dados.'
            )
            p_title('Quem deve utilizar o SMART PORTFOLIO ?')
            st.write(
                'Investidores que querem realizar uma análise independente da sua carteira de investimentos ou algum ativo'
                ' específico'
            )
            st.write('##')
            st.write(
                '''
                Link Mídias Sociais kkk
                '''
            )
            st.markdown(
                """
                [![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCHi_qOCcC_KeMu18cOyHtQg?style=social)](https://gitHub.com/dlopezyse/Synthia)
                """
                # [![Star](https: // img.shields.io / github / stars / dlopezyse / Synthia.svg?logo = instagram & style = social)](https: // gitHub.com / dlopezyse / Synthia)
                # [![DFGDFG](https: // img.shields.io / github / stars / dlopezyse / Synthia.svg?logo = linkedin & style = social)](https: // www.linkedin.com / in / david-sousa-ab6826198 /)
            )

        with right_column:
            st_lottie(lottie_coding, height=600, key='coding')

