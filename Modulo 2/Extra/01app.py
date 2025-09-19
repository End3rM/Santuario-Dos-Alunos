import streamlit as st 
import time

st.sidebar.title('Cálculo de IMC')
st.sidebar.write('Seja bem-vindo ao meu site, aqui você verá como apertar botões é engraçado e divertido. Grandes surpresas te aguardam, escolha com sabedoria!')
st.sidebar.image('2.png',width='content') 


# python -m streamlit run 01app.py

st.markdown("<h1 style='text-align: center;'>Por que a gente adora apertar um botãozinho?</h1>", unsafe_allow_html=True)

# conls = st.columns(2)
# conls[0].write('Nós, humanos, gostamos de ver o resultado das coisas:')
# conls[1].write('Coluna 2')

st.write('Somos criaturas curiosas e exploradoras; é natural em nós o desejo incomum de apertar botões. Aqui, "botões" não precisa ser literalmente um botão — pense como uma criança pensaria: por que ela quer experimentar tudo que toca? Para saber o gosto. Por que ela quebra as coisas? Para entender como elas reagem.') 
('Somos seres que reagem ao ambiente, portanto, a existência de um botão desperta nossa curiosidade. Ou seja, por que queremos tanto apertar os botões que encontramos pelo caminho? Exatamente para descobrir como funcionam e, se ativam algo, o que é que ativam. Interessante, não é? Que tal um pequeno experimento?')

st.markdown("<h1 style='text-align: center;'>Aperte alguns botões:</h1>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button('Botão A'):
        st.write('Sim, meu caro. A vida é curta, então não desperdice tempo se preocupando com o que não pode mudar.')

with col2:
    if st.button('Botão B'):
        st.write('Tudo o que um sonho precisa para ser realizado é alguém que acredite que ele possa ser realizado.')

with col3:
    if st.button('Botão D'):
        st.write('A sabedoria começa na reflexão.')

with col4:
    if st.button('Botão E'):
        st.write('Antes que pergunte "Onde está o C".. Não falamos do C.')

        temp_msg = st.empty()
        temp_msg.warning("Essa mensagem vai desaparecer em 3 segundos...")
        time.sleep(3)
        temp_msg.empty()

st.markdown("<h1 style='text-align: center;'>E aí, você gostou?</h1>", unsafe_allow_html=True)
resposta= st.text_input('Responda de maneira coerente. Seu Feedback nos fará crescer!')

if "sim" in resposta:
    st.write('Muito obrigada pelo Feedback positivo. Volte mais vezes se quiser acompanhar nosso crescimento.')
if "não" in resposta:
    st.write('Poxa. Tudo bem, entendemos sua opinião e lamentamos que sua experiência tenha sido ruim. Mande-nos um email se o problema for técnico.')
else:
    st.write('Tente novamente.')




