import uuid
import streamlit as st

from src.agent import EstudaiAgent

st.set_page_config(
    page_title="Estudai | Seu companheiro de estudos",
    page_icon="🎓",
    layout="wide"
)


if "agent" not in st.session_state:
    st.session_state.agent = EstudaiAgent()

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []


st.markdown("""
<style>

.stApp {
    background: #F5F7FC;
    color: #263445;
}

.main .block-container {
    max-width: 1100px;
    padding-top: 2.5rem;
    padding-bottom: 7rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #142D4E 0%, #0D2038 100%);
}

[data-testid="stSidebar"] * {
    color: #FFFFFF;
}

.sidebar-logo {
    font-size: 30px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 0;
}

.sidebar-subtitle {
    color: #B9C9DC !important;
    font-size: 14px;
    margin-top: -8px;
}

.sidebar-section {
    color: #AFC8E5 !important;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-top: 15px;
}

.main-title {
    color: #142D4E !important;
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin-bottom: 4px;
}

.main-subtitle {
    color: #718096 !important;
    font-size: 16px;
    margin-bottom: 25px;
}

.welcome-card {
    background: linear-gradient(135deg, #FFFFFF 0%, #EDF4FF 100%);
    border: 1px solid #DCE7F5;
    border-radius: 20px;
    padding: 38px 25px;
    text-align: center;
    box-shadow: 0 5px 20px rgba(20, 45, 78, 0.05);
    margin-top: 15px;
    margin-bottom: 30px;
}

.welcome-icon {
    font-size: 48px;
    margin-bottom: 10px;
}

.welcome-title {
    color: #142D4E !important;
    font-size: 27px;
    font-weight: 800;
    margin-bottom: 8px;
}

.welcome-description {
    color: #64748B !important;
    font-size: 15px;
    margin-bottom: 15px;
}

.welcome-highlight {
    color: #2463A6 !important;
    font-size: 15px;
    font-weight: 700;
}

.suggestion-title {
    color: #142D4E !important;
    font-size: 19px;
    font-weight: 750;
    margin-bottom: 12px;
}

.stButton > button {
    background: #FFFFFF;
    color: #2463A6 !important;
    border: 1px solid #DCE7F5;
    border-radius: 13px;
    padding: 12px 10px;
    min-height: 48px;
    font-weight: 700;
    transition: all 0.2s ease;
    box-shadow: 0 2px 7px rgba(20, 45, 78, 0.04);
}

.stButton > button p,
.stButton > button span,
.stButton > button div {
    color: #2463A6 !important;
    font-weight: 700;
}

.stButton > button:hover {
    background: #EAF2FF;
    border-color: #2463A6;
    transform: translateY(-2px);
}

.stButton > button:active {
    background: #DCEAFF;
}

[data-testid="stSidebar"] .stButton > button {
    background: #2463A6;
    border: 1px solid #477FB9;
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] .stButton > button p,
[data-testid="stSidebar"] .stButton > button span {
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: #3478C1;
    border-color: #70A6DF;
}

[data-testid="stChatMessage"] {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 12px;
    box-shadow: 0 3px 10px rgba(20, 45, 78, 0.035);
}

[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li {
    color: #263445;
    line-height: 1.7;
}

[data-testid="stChatInput"] {
    border-color: #DCE7F5;
}

[data-testid="stChatInput"] textarea {
    color: #263445 !important;
    background: #FFFFFF !important;
    caret-color: #2463A6;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #94A3B8 !important;
    opacity: 1;
}

[data-testid="stSpinner"] p {
    color: #2463A6 !important;
    font-weight: 600;
}

hr {
    border-color: rgba(255, 255, 255, 0.15);
}

@media (max-width: 768px) {
    .main .block-container {
        padding-top: 1.5rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .main-title {
        font-size: 29px;
    }

    .welcome-card {
        padding: 25px 15px;
    }

    .welcome-title {
        font-size: 22px;
    }
}

</style>
""", unsafe_allow_html=True)


with st.sidebar:

    st.markdown(
        '<div class="sidebar-logo">🎓 Estudai</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">Seu companheiro de estudos</div>',
        unsafe_allow_html=True
    )

    st.divider()

    if st.button("＋  Nova conversa", use_container_width=True):

        st.session_state.agent.clear_conversation(
            st.session_state.session_id
        )

        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())

        st.rerun()

    st.markdown(
        '<div class="sidebar-section">Seu espaço de estudos</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Aprenda, pratique e tire suas dúvidas no seu próprio ritmo."
    )

    st.divider()

    st.markdown(
        '<div class="sidebar-section">O que você pode fazer</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    📖  Aprender matérias escolares

    ✏️  Resolver exercícios

    🧠  Revisar conteúdos

    🔎  Tirar dúvidas
    """)

    st.divider()

    st.caption("ESTUDAI • PROJETO DE INTELIGÊNCIA ARTIFICIAL")


st.markdown(
    '<div class="main-title">Olá! Vamos estudar? 👋</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Aprender pode ser mais simples quando você tem '
    'a ajuda certa. Estou aqui para isso!'
    '</div>',
    unsafe_allow_html=True
)


if not st.session_state.messages:

    st.markdown("""
    <div class="welcome-card">
        <div class="welcome-icon">🎓</div>
        <div class="welcome-title">Bem-vindo ao Estudai!</div>
        <div class="welcome-description">
            Seu assistente inteligente está pronto para
            acompanhar sua jornada de aprendizagem.
        </div>
        <div class="welcome-highlight">
            O que você gostaria de aprender hoje?
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="suggestion-title">💡 Experimente começar por:</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(
            "📐  Matemática",
            use_container_width=True
        ):
            st.session_state.pending_prompt = (
                "Explique equações do primeiro grau."
            )
            st.rerun()

    with col2:
        if st.button(
            "🌎  História",
            use_container_width=True
        ):
            st.session_state.pending_prompt = (
                "Explique a Revolução Francesa."
            )
            st.rerun()

    with col3:
        if st.button(
            "🧬  Ciências",
            use_container_width=True
        ):
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


if prompt and prompt.strip():

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("O Estudai está preparando sua resposta..."):

            try:

                response = st.session_state.agent.chat(
                    prompt,
                    session_id=st.session_state.session_id
                )

                st.markdown(
                    response,
                    unsafe_allow_html=False
                )

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

            except Exception as error:

                st.error(
                    "Não foi possível obter uma resposta. "
                    "Verifique sua conexão e tente novamente."
                )

                st.caption(str(error))
