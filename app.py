import streamlit as st

st.set_page_config(
    page_title="Estudai",
    page_icon="🎓",
    layout="wide"
)


st.markdown("""
<style>

/* Fundo principal */
.stApp {
    background-color: #F4F7FB;
    color: #263445;
}

/* Textos gerais */
.stApp p,
.stApp h1,
.stApp h2,
.stApp h3,
.stMarkdown,
.stMarkdown p,
.stMarkdown li {
    color: #263445;
}

/* Menu lateral */
[data-testid="stSidebar"] {
    background-color: #142D4E;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* Título */
.titulo {
    color: #142D4E !important;
    font-size: 38px;
    font-weight: bold;
}

.subtitulo {
    color: #64748B !important;
    font-size: 17px;
}

/* Boas-vindas */
.boas-vindas {
    background-color: #FFFFFF;
    border-radius: 15px;
    padding: 30px;
    text-align: center;
    border: 1px solid #E2E8F0;
}

.boas-vindas h2 {
    color: #142D4E !important;
}

.boas-vindas p {
    color: #64748B !important;
}

/* Mensagens do chat */
[data-testid="stChatMessage"] {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    color: #263445 !important;
}

[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] .stMarkdown {
    color: #263445 !important;
}

[data-testid="stChatInput"] textarea {
    color: #263445 !important;
    background-color: #FFFFFF !important;
    caret-color: #2463A6 !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #94A3B8 !important;
    opacity: 1 !important;
}

.stButton > button {
    background-color: #2463A6 !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px;
    font-weight: 700 !important;
    transition: 0.2s;
}

.stButton > button p,
.stButton > button span,
.stButton > button div {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    background-color: #142D4E !important;
    border: none !important;
}

.stButton > button:active {
    background-color: #0D2038 !important;
}

</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:

    st.markdown("# 🎓 Estudai")

    st.caption("Seu companheiro de estudos")

    st.divider()

    if st.button("＋ Nova conversa", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("### 📚 Espaço de estudos")

    st.write("Tire dúvidas e aprenda no seu próprio ritmo.")

    st.divider()

    st.markdown("### 💡 Você pode:")

    st.write("📖 Aprender matérias escolares")
    st.write("✏️ Resolver exercícios")
    st.write("🧠 Revisar conteúdos")
    st.write("🔎 Tirar dúvidas")

    st.divider()

    st.caption("Estudai | Projeto de IA")

st.markdown(
    '<div class="titulo">Olá! Vamos estudar? 🎓</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">'
    'Estou aqui para ajudar você a aprender '
    'de forma simples e acessível.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")

if not st.session_state.messages:

    st.write("")

    # Caixa de boas-vindas
    with st.container(border=True):

        st.markdown(
            "<h2 style='color:#142D4E; text-align:center;'>"
            "Bem-vindo ao Estudai! 🎓"
            "</h2>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<p style='color:#64748B; text-align:center;'>"
            "Seu companheiro de estudos está pronto "
            "para ajudar você."
            "</p>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<h1 style='text-align:center;'>"
            "📚 ✏️ 🧠"
            "</h1>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<p style='color:#2463A6; text-align:center; "
            "font-weight:bold;'>"
            "O que você gostaria de aprender hoje?"
            "</p>",
            unsafe_allow_html=True
        )

    st.write("")

    st.markdown("### Experimente perguntar:")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📐 Matemática", use_container_width=True):
            st.session_state.pending_prompt = (
                "Explique equações do primeiro grau."
            )
            st.rerun()

    with col2:
        if st.button("🌎 História", use_container_width=True):
            st.session_state.pending_prompt = (
                "Explique a Revolução Francesa."
            )
            st.rerun()

    with col3:
        if st.button("🧬 Ciências", use_container_width=True):
            st.session_state.pending_prompt = (
                "Como funciona a fotossíntese?"
            )
            st.rerun()

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input(
    "Digite sua dúvida ou exercício..."
)

if "pending_prompt" in st.session_state:
    prompt = st.session_state.pop("pending_prompt")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Estudai está pensando..."):

            try:
                from src.agent import generate_response

                response = generate_response(
                    st.session_state.messages
                )

                st.markdown(response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

            except Exception as error:

                st.error(
                    "Não foi possível obter a resposta. "
                    "Verifique a integração com o agente."
                )

                st.caption(str(error))