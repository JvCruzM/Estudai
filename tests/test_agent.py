from src.agent import EstudaiAgent

def main():

    print("=" * 45)
    print("          ESTUDAI - ASSISTENTE IA")
    print("=" * 45)

    # Inicializa o agente
    agent = EstudaiAgent()

    # Identificador da conversa
    session_id = "teste_usuario"

    print("\nEstudai: Olá! Sou o Estudai.")
    print("Vamos aprender juntos!")
    print("Digite 'sair' para encerrar.")
    print("Digite 'limpar' para reiniciar a conversa.\n")

    while True:

        question = input("Você: ").strip()

        if question.lower() == "sair":
            print("\nEstudai: Bons estudos! Até mais!")
            break

        if question.lower() == "limpar":
            agent.clear_conversation(session_id)
            print("\nEstudai: Nossa conversa foi reiniciada!\n")
            continue

        answer = agent.chat(
            question,
            session_id=session_id
        )

        print(f"\nEstudai: {answer}\n")


if __name__ == "__main__":
    main()
