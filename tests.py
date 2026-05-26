# tests para ver si el bot funciona

from rag_core import build_rag, preguntar

db, client = build_rag()

tests = [
    ("¿hacen envíos a Córdoba?", "andreani"),
    ("¿cuánto tarda el envío?", "días"),
    ("¿la ropa es de buena calidad?", "1111111111"),       # debe derivar
    ("¿tienen local físico?", "online"),
    ("¿aceptan Mercado Pago?", "mercado"),
    ("¿matarías a alguien?", "1111111111"),                 # debe derivar
    ("¿tienen talles grandes?", "xxl"),
    ("¿puedo pagar en cuotas?", "cuotas"),
    ("¿tienen ropa de mujer?", "mujer"),
    ("¿cómo hago un cambio?", "30"),
]

print("=== QA TEST URBAN THREAD BOT ===\n")
pasados = 0

for pregunta, palabra_esperada in tests:
    respuesta = preguntar(db, client, pregunta)
    ok = palabra_esperada.lower() in respuesta.lower()
    estado = "✓ PASS" if ok else "✗ FAIL"
    if ok:
        pasados += 1
    print(f"{estado} | {pregunta}")
    print(f"       Respuesta: {respuesta[:120]}...\n")

print(f"Resultado: {pasados}/{len(tests)} tests pasados")
