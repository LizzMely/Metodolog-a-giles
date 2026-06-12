from clasificador import clasificar_sentimiento, limpiar_texto, generar_reporte

def test_limpieza():
    assert limpiar_texto("¡Excelente!!!") == "excelente"
    assert limpiar_texto("Muy SUCIO??") == "muy sucio"

def test_clasificacion():
    assert clasificar_sentimiento("Excelente servicio") == "Positiva"
    assert clasificar_sentimiento("Habitación sucia") == "Negativa"
    assert clasificar_sentimiento("Todo bien") == "Positiva"
    assert clasificar_sentimiento("Nada especial") == "Neutral"

def test_reporte():
    datos = [("bueno", "Positiva"), ("malo", "Negativa"), ("nada", "Neutral")]
    reporte = generar_reporte(datos)
    assert reporte["positivas"] == 1
    assert reporte["negativas"] == 1
    assert reporte["neutrales"] == 1
    assert reporte["total"] == 3
