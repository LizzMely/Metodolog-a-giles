# Taller Día 5 – Metodologías Ágiles
Este repositorio contiene el código del taller integrador del Día 5, donde se aplican **Scrum, Kanban y XP** para construir un sistema que clasifica reseñas de clientes de un hotel.

## Ejecución de proyecto

### 1. Ejecutar pruebas (TDD)
python test_clasificador.py

##2. Ejecutar el sistema principal
python main.py

📁 Archivos incluidos
clasificador.py → Lógica de limpieza, clasificación y generación de reporte
test_clasificador.py → Pruebas unitarias (TDD)
main.py → Script principal que procesa el archivo
reseñas.txt → Archivo con 20 reseñas de clientes
LÉAME.md → Documentación del proyecto

🧪 Metodologías aplicadas
✔ Scrum
Backlog priorizado
Sprint de 4 horas
Roles definidos

✔ Kanban
WIP = 2
Flujo visible en el tablero

✔ XP
TDD (pruebas antes del código)
Refactorización
Programación por pares

📊 Funcionalidad del sistema
El sistema:
Lee 20 reseñas desde un archivo .txt
Limpia el texto

Clasifica cada reseña como:
Positiva
Negativa
Neutral

Genera un reporte final con estadísticas simples:
Total positivas
Total negativas
Total neutrales


Total general
