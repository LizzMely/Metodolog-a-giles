import re

positivas = ["bueno", "excelente", "genial", "limpio", "amable", "perfecto", "agradable"]
negativas = ["malo", "sucio", "tarde", "roto", "feo", "horrible", "terrible"]

def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúñü\s]", "", texto)
    return texto.strip()

def clasificar_sentimiento(texto):
    texto_limpio = limpiar_texto(texto)

    if any(p in texto_limpio for p in positivas):
        return "Positiva"
    if any(n in texto_limpio for n in negativas):
        return "Negativa"
    return "Neutral"

def procesar_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    resultados = []
    for linea in lineas:
        if linea.strip():
            sentimiento = clasificar_sentimiento(linea)
            resultados.append((linea.strip(), sentimiento))
    return resultados

def generar_reporte(resultados):
    positivas = sum(1 for _, s in resultados if s == "Positiva")
    negativas = sum(1 for _, s in resultados if s == "Negativa")
    neutrales = sum(1 for _, s in resultados if s == "Neutral")

    return {
        "positivas": positivas,
        "negativas": negativas,
        "neutrales": neutrales,
        "total": len(resultados)
    }
