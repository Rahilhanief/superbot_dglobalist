# AI Chatbot for Indian Unicorn Startups (LangChain)

This project implements a **Python-based AI chatbot** that answers questions about **Indian unicorn startups** using a **static Kaggle dataset**, while maintaining **conversation context**, asking **clarifying questions for ambiguous queries**, and demonstrating **product-quality engineering practices** like sanitization, logging, and observability.

The chatbot is built using the **LangChain framework** and a lightweight **GenAI stack**.

---

##  Features

*  **Static Knowledge Base**: Uses a Kaggle dataset of Indian unicorn startups (no live web search)
*  **Conversational Memory**: Maintains context across multiple user turns
*  **Clarification Logic**: Asks follow-up questions for vague or underspecified queries
*  **Semantic Search**: Vector-based retrieval over company data
*  **Query Sanitization**: Input normalization and basic prompt-injection protection
*  **Structured Logging**: Logs queries, responses, timestamps, and session IDs
*  **Observability (Lightweight)**: Tracks metrics like query count and clarification count

---

##  Architecture Overview

```
User Query
   ↓
Sanitization Layer
   ↓
Clarification Detection (LLM-based)
   ↓
LangChain Retrieval (Vector Store)
   ↓
Conversation Memory
   ↓
LLM Response Generation
   ↓
Logging + Metrics (Langfuse-ready)
```

---

##  Project Structure

```
.
├── app.py                # CLI chatbot entry point
├── data_loader.py        # Loads & preprocesses Kaggle dataset
├── chatbot.py            # LangChain chatbot logic
├── sanitizer.py          # Input sanitization utilities
├── logger.py             # Structured logging
├── observability.py            # Lightweight observability counters
├── requirements.txt      # Python dependencies
├── data/
│   └── unicorns.csv      # Kaggle dataset (download separately)
└── README.md
```

---

##  Dataset Setup

1. Download the dataset from Kaggle:
   [https://www.kaggle.com/datasets/srisankargiri/list-of-118-unicorn-startups-in-indiamay-2025](https://www.kaggle.com/datasets/srisankargiri/list-of-118-unicorn-startups-in-indiamay-2025)

2. Extract and place the CSV file as:

```
data/unicorns.csv
```

> ⚠️ The chatbot **will not work** without this file.

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ai-unicorn-chatbot
```

### 2. Create & Activate Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\\Scripts\\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file or export variables:

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

(Optional – for observability):

```bash
export LANGFUSE_PUBLIC_KEY="your_langfuse_public_key"
export LANGFUSE_SECRET_KEY="your_langfuse_secret_key"
export LANGFUSE_HOST="https://cloud.langfuse.com"
```

---

## ▶ How to Run the Chatbot

Run the CLI chatbot:

```bash
python app.py
```

You should see:

```
 Unicorn Chatbot Ready! Type 'exit' to quit.
```

---

##  Sample Interaction

```
User: Tell me about fintech unicorns
Bot: Here are some fintech unicorn startups in India: Razorpay, PhonePe, CRED...

User: Which of these are based in Bangalore?
Bot: Razorpay and CRED are based in Bangalore.

User: Which company is best to collaborate with?
Bot: Can you clarify the type of collaboration you are looking for (e.g., fintech, logistics, SaaS)?
```

---

##  Observability & Metrics

The chatbot tracks:

* Total number of queries
* Number of clarification questions asked
* Errors or fallback responses
* (Optional) Latency per response

Metrics are printed periodically and designed to be easily wired into **Langfuse**.

---

---

##  Author

**Rahil Hanief Bhat**

---
