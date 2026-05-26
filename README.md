# Urban Thread AI Chatbot

RAG-powered customer service chatbot for an e-commerce clothing store.

## What it does

Answers customer questions (shipping, sizing, returns, payment methods) using only the store's actual data — no hallucinations, no invented information. Out-of-scope questions are redirected to human support.

## Tech stack

- **Python** — core logic
- **LangChain** — document loading and text splitting
- **ChromaDB** — vector database for semantic search
- **HuggingFace Embeddings** — sentence-transformers/all-MiniLM-L6-v2
- **Groq API (LLaMA 3.1)** — language model
- **Streamlit** — web interface

## How it works

1. Store data (`datos.txt`) is split into chunks and converted to embeddings
2. On each user query, the 3 most semantically similar chunks are retrieved
3. Those chunks are passed as context to the LLM with a strict system prompt
4. The model answers using only the provided context

## Run locally

```bash
pip install -r requirements.txt
export GROQ_API_KEY=your_key_here
streamlit run bot2.py
```

## Project structure

```
├── rag_core.py      # Core RAG logic
├── bot.py           # Terminal interface
├── bot2.py          # Streamlit web interface
├── datos.txt        # Store knowledge base
├── tests.py         # QA tests
└── requirements.txt
```
