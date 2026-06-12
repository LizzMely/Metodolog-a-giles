from clasificador import procesar_archivo, generar_reporte

if __name__ == "__main__":
    resultados = procesar_archivo("reseñas.txt")

    print("\n📊 Resultados de clasificación:")
    for texto, sentimiento in resultados:
        print(f"- {texto} → {sentimiento}")

    reporte = generar_reporte(resultados)

    print("\n📈 Estadísticas:")
    print(f"Positivas: {reporte['positivas']}")
    print(f"Negativas: {reporte['negativas']}")
    print(f"Neutrales: {reporte['neutrales']}")
    print(f"Total: {reporte['total']}")
