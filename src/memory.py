from langchain_core.messages import HumanMessage, AIMessage

class ConversationMemory:
    """
    Gerencia o histórico de conversas do Estudai.

    Cada session_id representa uma conversa independente.
    O histórico permanece em memória durante a execução.
    """

    def __init__(self, max_messages=20):
        self.sessions = {}
        self.max_messages = max_messages

    def get_history(self, session_id):
        if session_id not in self.sessions:
            self.sessions[session_id] = []

        return self.sessions[session_id]

    def add_messages(self, session_id, user_message, ai_response):
        history = self.get_history(session_id)

        history.append(HumanMessage(content=user_message))
        history.append(AIMessage(content=ai_response))

        # Mantém somente as últimas mensagens.
        if len(history) > self.max_messages:
            self.sessions[session_id] = history[-self.max_messages:]

    def clear_history(self, session_id):
        if session_id in self.sessions:
            self.sessions[session_id] = []
