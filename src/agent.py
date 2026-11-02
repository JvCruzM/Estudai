import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

from src.prompts import SYSTEM_PROMPT
from src.memory import ConversationMemory


# Carrega as configurações do arquivo .env
load_dotenv()


class EstudaiAgent:
    """
    Agente educacional Estudai.

    Responsável por:
    - Conectar ao modelo de linguagem.
    - Interpretar perguntas dos estudantes.
    - Aplicar as instruções educacionais.
    - Manter o contexto das conversas.
    """

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY não encontrada. "
                "Configure sua chave no arquivo .env."
            )

        model_name = os.getenv(
            "GROQ_MODEL",
            "openai/gpt-oss-20b"
        )

        # Inicializa o modelo de inteligência artificial
        self.llm = ChatGroq(
            model=model_name,
            api_key=api_key,
            temperature=0.3,
            max_retries=2
        )

        # Inicializa a memória das conversas
        self.memory = ConversationMemory(
            max_messages=20
        )

        # Organiza as instruções e mensagens
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),

            MessagesPlaceholder(
                variable_name="history"
            ),

            ("human", "{question}")
        ])

        # Conecta o prompt ao modelo
        self.chain = self.prompt | self.llm

    def chat(self, question, session_id="default"):
        """
        Recebe uma pergunta e retorna uma resposta do Estudai.
        """

        if not question or not question.strip():
            return "Digite uma pergunta para começarmos!"

        try:
            # Recupera o histórico da conversa
            history = self.memory.get_history(session_id)

            # Envia a pergunta e o contexto ao modelo
            response = self.chain.invoke({
                "history": history,
                "question": question
            })

            answer = response.content

            # Garante que a resposta seja texto
            if not isinstance(answer, str):
                answer = str(answer)

            # Salva a interação na memória
            self.memory.add_messages(
                session_id,
                question,
                answer
            )

            return answer

        except Exception as error:
            print(f"Erro no Estudai: {error}")

            return (
                "Desculpe! Tive um problema ao processar "
                "sua pergunta. Verifique sua conexão e "
                "tente novamente."
            )

    def clear_conversation(self, session_id="default"):
        """
        Limpa o histórico de uma conversa específica.
        """
        self.memory.clear_history(session_id)
