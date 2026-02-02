from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory

from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI

from observability import langfuse_handler
def create_chatbot(retriever):
    """
    Creates a conversational RAG chatbot using latest LangChain APIs.
    """

    # -------------------------
    # Prompt
    # -------------------------
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an AI assistant answering questions about Indian unicorn startups. "
            "Use ONLY the provided context. Do not hallucinate."
        ),
        (
            "human",
            """
Conversation history:
{history}

Context:
{context}

Question:
{input}

Answer clearly and concisely.
"""
        ),
    ])

    # -------------------------
    # LLM
    # -------------------------
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2,
        callbacks=[langfuse_handler],
    )

    # -------------------------
    # Retrieval helper
    # -------------------------
    def retrieve_context(inputs: str) -> str:
        query = inputs["input"]  # ✅ extract string
        docs = retriever.invoke(query)
        return "\n\n".join(d.page_content for d in docs)

    # -------------------------
    # LCEL Chain (NO LLMChain)
    # -------------------------
    rag_chain = (
    {
        "context": retrieve_context,
        "input": lambda x: x["input"],      # ✅ string only
        "history": lambda x: x["history"],  # ✅ history only
    }
    | prompt
    | llm
    | StrOutputParser()
)


    # -------------------------
    # Conversation History Store
    # -------------------------
    store = {}

    def get_session_history(session_id: str):
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]

    # -------------------------
    # Memory-enabled Runnable
    # -------------------------
    chatbot = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )


    # -------------------------
    # Public Chat Function
    # -------------------------
    def chat(query: str, session_id: str = "default"):
        return chatbot.invoke(
            {"input": query},
            config={"configurable": {"session_id": session_id}},
        )

    return chat
