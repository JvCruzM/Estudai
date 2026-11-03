# 🎓 Estudai

**Seu companheiro inteligente de estudos!**

O Estudai é um assistente educacional desenvolvido com Inteligência Artificial, projetado para auxiliar estudantes no aprendizado de conteúdos escolares, resolução de exercícios e esclarecimento de dúvidas.

Nosso objetivo é tornar o aprendizado mais simples, acessível e interativo, oferecendo explicações didáticas e adaptadas às necessidades de cada estudante.

## ✨ Funcionalidades

- 📚 Explicação de conteúdos escolares.
- ✏️ Resolução de exercícios passo a passo.
- 🧠 Revisão e reforço de aprendizagem.
- 💬 Conversação com histórico e memória de contexto.
- 🎯 Respostas adaptadas ao ritmo de aprendizagem do estudante.
- 🌐 Interface interativa desenvolvida com Streamlit.

## 🛠️ Tecnologias utilizadas

- **Python 3.12** — Linguagem de programação.
- **LangChain** — Integração e gerenciamento das interações com o modelo de IA.
- **Groq API** — Acesso ao modelo de Inteligência Artificial.
- **Streamlit** — Desenvolvimento da interface web.
- **Python-dotenv** — Gerenciamento de variáveis de ambiente.

## 📋 Pré-requisitos

Antes de executar o projeto, certifique-se de possuir:

- Python 3.12 instalado.
- Git instalado (caso queira clonar o repositório).
- Conexão com a internet.
- Uma chave de API da Groq.

## 🚀 Instalação e configuração

### 1. Clone o repositório

```bash
git clone https://github.com/JvCruzM/Estudai.git
```

### 2. Acesse a pasta do projeto

```bash
cd Estudai
```

### 3. Crie o ambiente virtual

Na raiz do projeto, execute:

```bash
python -m venv venv
```

Esse comando cria um ambiente virtual para manter as dependências do projeto isoladas.

### 4. Ative o ambiente virtual

No Windows PowerShell, execute:

```powershell
.\venv\Scripts\Activate.ps1
```

Após a ativação, o terminal deverá apresentar `(venv)` no início da linha.

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

Esse comando instala todas as bibliotecas necessárias para executar o Estudai.

### 6. Configure a chave da API

Crie um arquivo chamado `.env` na raiz do projeto, utilizando o `.env.example` como referência, caso esteja disponível.

Configure as seguintes variáveis:

```env
GROQ_API_KEY=sua_chave_api
GROQ_MODEL=openai/gpt-oss-20b
```

Substitua `sua_chave_api` pela sua chave pessoal da Groq.

**Importante:** nunca compartilhe sua chave de API ou envie o arquivo `.env` para o GitHub.

## 💻 Como executar o agente pelo terminal

Para utilizar o Estudai diretamente no terminal, com uma interface de conversação em texto, execute na raiz do projeto:

```bash
python -m tests.test_agent
```

Após iniciar, você poderá digitar suas perguntas e receber respostas diretamente pelo terminal.

**Comandos disponíveis durante a conversa:**

- `sair` — Encerra a execução do agente.
- `limpar` — Reinicia o histórico da conversa.

## 🌐 Como executar a interface web

Para utilizar o Estudai por meio de sua interface gráfica, execute:

```bash
python -m streamlit run app.py
```

Após a execução, o Streamlit disponibilizará o endereço local da aplicação no terminal e abrirá a interface no navegador.

**Observação:** caso o Streamlit solicite um endereço de e-mail na primeira execução, basta pressionar `Enter` para continuar sem informar um e-mail.

Pronto! Agora você poderá conversar com o Estudai diretamente pelo navegador.

## 📁 Estrutura do projeto

```text
Estudai/
│
├── src/
│   ├── agent.py
│   ├── memory.py
│   └── prompts.py
│
├── tests/
│   └── test_agent.py
│
├── app.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
```

**Descrição dos principais arquivos:**

| Arquivo | Responsabilidade |
|---|---|
| `agent.py` | Configuração e funcionamento do agente de IA. |
| `memory.py` | Gerenciamento do histórico das conversas. |
| `prompts.py` | Definição das instruções e comportamento do Estudai. |
| `test_agent.py` | Execução do agente pelo terminal. |
| `app.py` | Interface web desenvolvida com Streamlit. |
| `requirements.txt` | Lista de dependências do projeto. |
| `.env` | Armazenamento das variáveis de ambiente. |

## ⚙️ Comandos úteis

| Comando | Finalidade |
|---|---|
| `python --version` | Verifica a versão do Python. |
| `python -m venv venv` | Cria o ambiente virtual. |
| `.\venv\Scripts\Activate.ps1` | Ativa o ambiente virtual. |
| `pip install -r requirements.txt` | Instala as dependências. |
| `python -m tests.test_agent` | Executa o agente no terminal. |
| `python -m streamlit run app.py` | Inicia a interface web. |

## 👥 Equipe de desenvolvimento

**Projeto desenvolvido como atividade acadêmica.**

- João Vitor Cruz de Menezes
- Elidiane Moniky Vitória Nunes da Silva
- Jamilly Vitória dos Santos Silva

---

<p align="center">
  🎓 <strong>Estudai — Aprender nunca foi tão acessível!</strong>
</p>
