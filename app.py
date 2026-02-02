import uuid
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from loader import load_documents
from vectostore import create_vectorstore  # fixed typo
from chatbot import create_chatbot
from clarifier import needs_clarification
from sanitizer import sanitize_query
from logger import log_interaction

app = FastAPI(title="Unicorn Chatbot API")

# Optional: allow cross-origin requests if using frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load dataset and initialize chatbot at startup
csv_path = os.path.join("data", "tracxn.csv")
docs = load_documents(csv_path)
print(f"Loaded {len(docs)} documents.")

db = create_vectorstore(docs)
retriever = db.as_retriever(search_kwargs={"k": 4})
chatbot = create_chatbot(retriever)


@app.post("/chat")
def chat(query: str, session_id: str | None = None):
    """
    Chat endpoint
    - query: user question
    - session_id: optional for conversation tracking
    """
    session_id = session_id or str(uuid.uuid4())
    query = sanitize_query(query)

    if needs_clarification(query):
        response = (
            "Can you clarify the type of collaboration you are looking for "
            "(e.g., payments, logistics, technology)?"
        )
    else:
        response = chatbot(query)

    log_interaction(session_id, query, response)

    return {"session_id": session_id, "response": response}


# Optional CLI mode for testing
if __name__ == "__main__":
    print("\nChatbot CLI ready! Type 'exit' to quit.\n")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting...")
            break
        answer = chatbot(query)
        print("Bot:", answer)
