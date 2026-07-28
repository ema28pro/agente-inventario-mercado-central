# 🛒 Agente Inteligente - Mercado Central 24h

Agente de inteligencia artificial que responde preguntas en lenguaje natural sobre el inventario de **Mercado Central 24h**, un supermercado de operación continua. Permite a cualquier persona colaboradora consultar stock, precios, proveedores y vencimientos sin abrir manualmente el archivo de inventario.

> Proyecto desarrollado como parte del **Challenge Alura Agente** — Programa ONE Agentes + AluraLatam.

---

## 📋 Descripción general

La empresa cuenta con un archivo de inventario (`inventario.xlsx`) con 200 productos y 18 atributos por producto (stock, precios, categoría, proveedor, fechas de vencimiento, etc.). En lugar de que el personal busque manualmente en la hoja de cálculo, este agente permite hacer preguntas directas como *"¿qué productos tienen stock por debajo del mínimo?"* y recibir una respuesta clara en español.

## 🏗️ Arquitectura de la solución

```
Usuario (navegador)
        │
        ▼
  Interfaz Streamlit (chat)
        │
        ▼
  Agente LangChain (pandas dataframe agent)
        │
        ├──► Pandas DataFrame (inventario.xlsx cargado en memoria)
        │
        ▼
  LLM: Google Gemini (gemini-3.5-flash-lite / gemini-3.6-flash)
        │
        ▼
  Respuesta en lenguaje natural
```

**Flujo:**
1. El archivo `inventario.xlsx` se carga en un DataFrame de Pandas al iniciar la app.
2. El usuario escribe una pregunta en la interfaz de chat de Streamlit.
3. LangChain usa un **pandas dataframe agent**, que traduce la pregunta en operaciones sobre el DataFrame (filtros, agregaciones, ordenamientos) ejecutando código Python internamente.
4. El LLM (Gemini 3.5 Flash-Lite / 3.6 Flash) interpreta el resultado y genera una respuesta en lenguaje natural.
5. La respuesta se muestra en la interfaz interactiva del chat.

> **¿Por qué un pandas agent y no RAG con embeddings?** El documento fuente es tabular (no texto libre), así que un agente que razona directamente sobre la tabla es más preciso y rápido que fragmentar el archivo en chunks vectorizados. Esto es una decisión de arquitectura justificada por el tipo de dato, no un atajo.

## 🛠️ Tecnologías utilizadas

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.11+ |
| Orquestación del agente | LangChain (`langchain-experimental`) |
| Modelo de lenguaje | Google Gemini 3.5 Flash-Lite / Gemini 3.6 Flash (familia Gemini 3.x vigente) |
| Procesamiento de datos | Pandas |
| Interfaz | Streamlit |
| Deploy | Streamlit Community Cloud |
| Control de versiones | Git / GitHub |

## 📂 Estructura del repositorio

```
agente-inventario-mercado-central/
├── app/
│   ├── app.py              # Aplicación principal (Streamlit + agente)
│   └── inventario.xlsx     # Dataset fuente de 200 productos
├── docs/
│   └── ejemplos.md         # Registro completo de preguntas y respuestas reales
├── assets/
│   └── deploy-screenshot.png  # Captura de pantalla del despliegue en producción
├── requirements.txt        # Dependencias de Python
├── .env.example            # Plantilla para variables de entorno
├── .gitignore              # Configuración de archivos excluidos de Git
└── README.md               # Documentación del proyecto
```

## ▶️ Instrucciones para ejecutar el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/ema28pro/agente-inventario-mercado-central.git
cd agente-inventario-mercado-central
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar la API Key
Copia `.env.example` a `.env` y agrega tu API Key gratuita de Gemini (consíguela en https://aistudio.google.com/apikey):
```
GOOGLE_API_KEY=tu_api_key_aqui
```

### 4. Ejecutar la aplicación
```bash
streamlit run app/app.py
```
La app se abrirá automáticamente en `http://localhost:8501`.

## 💬 Ejemplos de preguntas que el agente puede responder

- ¿Cuántos productos hay en total en el inventario?
- ¿Cuál es el producto con mayor stock actual?
- ¿Qué productos están por debajo de su stock mínimo?
- ¿Cuál es el precio promedio de los productos de la categoría Lácteos?
- ¿Qué producto tiene el margen de ganancia más alto (precio de venta menos costo unitario)?
- ¿Cuántos proveedores distintos abastecen el inventario?
- ¿Qué productos vencen antes de una fecha determinada?
- ¿Cuál es el proveedor con más productos suministrados?

## 🖼️ Ejemplos de respuestas generadas

| Pregunta | Respuesta del Agente |
|---|---|
| **¿Cuántos productos hay en total en el inventario?** | El inventario cuenta con un total de **200 productos** registrados en Mercado Central 24h. |
| **¿Cuál es el producto con mayor stock actual?** | El producto con mayor stock actual es **Cerveza Clara Lata 355ml**, con un stock disponible de **500 unidades**. |
| **¿Qué productos están por debajo de su stock mínimo?** | Actualmente **no hay productos** por debajo de su nivel de stock mínimo. |
| **¿Cuál es el precio promedio de la categoría Lácteos?** | El precio promedio de los productos de la categoría Lácteos es de **$13.00**. |
| **¿Qué producto tiene el mayor margen de ganancia?** | **Queso Oaxaca / Mozzarella Trozo** tiene el margen más alto: **$34.90** por unidad ($89.90 venta − $55.00 costo). |
| **¿Cuál es el proveedor con más productos suministrados?** | **Sigma Alimentos**, abasteciendo **15 productos** diferentes. |

> Consulta el documento [docs/ejemplos.md](docs/ejemplos.md) para ver la lista extendida de respuestas.

## ☁️ Evidencia del Deploy

- 🔗 **Aplicación desplegada:** [https://agente-inventario-mercado-central.streamlit.app](https://agente-inventario-mercado-central.streamlit.app)
- 📸 **Captura de pantalla:** Guardada en `assets/deploy-screenshot.png`.

## 📌 Notas del proyecto

Este proyecto prioriza la precisión de las respuestas del agente sobre el dataset tabular de inventarios, utilizando un diseño de chat fluido y reactivo con Streamlit.
