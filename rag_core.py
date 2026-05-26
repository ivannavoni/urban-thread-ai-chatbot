# logica del programa

import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from groq import Groq

DATA_PATH = "datos.txt"
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_MODEL = "llama-3.1-8b-instant"

SYSTEM_PROMPT = """Sos el asistente virtual de Urban Thread, tienda de ropa urbana online.

Tu función es ayudar a los clientes a encontrar lo que buscan y resolver sus dudas.

Reglas estrictas:
- Respondé SOLO usando la información del contexto proporcionado.
- Si no tenés la información, decí exactamente: "No tengo esa info, escribinos por WhatsApp al 1156781234 o a hola@urbanthread.com.ar"
- NUNCA inventes precios, productos, talles ni políticas.
- No respondas preguntas que no tengan nada que ver con la tienda.
- Respondé siempre en español rioplatense (vos, tenés, etc.), de forma corta, directa y amable.
- Si el cliente duda sobre un talle o producto, sugerile que nos contacte por WhatsApp para asesoramiento personalizado."""

def build_rag():
    loader = TextLoader(DATA_PATH, encoding="utf-8")
    docs = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(chunks, embeddings)

    client = Groq(api_key=GROQ_API_KEY)

    return db, client

def preguntar(db, client, pregunta: str) -> str:
    resultados = db.similarity_search(pregunta, k=3)
    contexto = "\n".join([d.page_content for d in resultados])

    respuesta = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Contexto:\n{contexto}\n\nPregunta: {pregunta}"}
        ]
    )
    return respuesta.choices[0].message.content