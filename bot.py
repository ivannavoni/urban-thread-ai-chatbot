# interfaz de terminal

from rag_core import build_rag, preguntar

db, client = build_rag()

print("Urban Thread Bot listo. Escribí tu pregunta (o 'salir' para terminar):\n")

while True:
    pregunta = input("Vos: ")
    if pregunta.lower() == "salir":
        break

    respuesta = preguntar(db, client, pregunta)
    print(f"\nBot: {respuesta}\n")