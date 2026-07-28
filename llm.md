# llm.md — Instrucciones para el agente de desarrollo

## Contexto
Estoy terminando el **Challenge Alura Agente** (ONE + AluraLatam) con muy poco tiempo disponible. Ya tengo la base del proyecto armada (estructura, `app.py`, `README.md`, `requirements.txt`). Necesito que completes, valides y dejes listo para producción lo que falta. Prioriza que funcione sobre que sea perfecto.

## Qué es el proyecto
Agente de IA que responde preguntas en lenguaje natural sobre `app/inventario.xlsx` (200 productos de un supermercado: stock, precios, categorías, proveedores, vencimientos). Usa LangChain (`create_pandas_dataframe_agent`) + Gemini (`gemini-1.5-flash`) + Streamlit como interfaz y capa de deploy.

## Estructura ya existente
```
agente-inventario-mercado-central/
├── app/
│   ├── app.py              # YA EXISTE — revisar y corregir si hay errores
│   └── inventario.xlsx     # YA EXISTE
├── docs/
│   └── ejemplos.md         # plantilla vacía — llenar con respuestas reales
├── assets/                 # vacía — aquí va la captura del deploy
├── requirements.txt        # YA EXISTE
├── .env.example             # YA EXISTE
├── .gitignore               # YA EXISTE
└── README.md                # YA EXISTE — actualizar secciones marcadas como pendientes
```

## Tareas, en orden de prioridad

### 1. Validar y correr el agente localmente (crítico)
- Instalar dependencias de `requirements.txt`.
- Confirmar que `app/app.py` carga `inventario.xlsx` sin errores.
- Ejecutar `streamlit run app/app.py` y probar mínimo estas 8 preguntas (están en el README):
  1. ¿Cuántos productos hay en total en el inventario?
  2. ¿Cuál es el producto con mayor stock actual?
  3. ¿Qué productos están por debajo de su stock mínimo?
  4. ¿Cuál es el precio promedio de los productos de la categoría Lácteos?
  5. ¿Qué producto tiene el margen de ganancia más alto (Precio de Venta Unitario − Costo Unitario)?
  6. ¿Cuántos proveedores distintos abastecen el inventario?
  7. ¿Qué productos vencen antes de una fecha determinada?
  8. ¿Cuál es el proveedor con más productos suministrados?
- Si alguna pregunta falla o da resultado incoherente, ajustar el prompt del agente o el manejo de tipos de columnas (ojo: la columna `Fecha de Vencimiento` puede venir como texto mezclado con fechas — normalizar con `pd.to_datetime(..., errors="coerce")` si es necesario).
- Pegar las respuestas reales obtenidas en `docs/ejemplos.md`, reemplazando los placeholders.
- Copiar 2-3 de las mejores respuestas también a la sección "Ejemplos de respuestas generadas" del `README.md`.

### 2. Preparar el repositorio GitHub (crítico)
- Repo público, nombre: `agente-inventario-mercado-central`.
- Verificar que `.env` (con la key real) **no** se suba — ya está en `.gitignore`, confirmar.
- Hacer commits incrementales y descriptivos (no un solo commit gigante), por ejemplo:
  - `chore: estructura inicial del proyecto`
  - `feat: agente pandas + integración con Gemini`
  - `feat: interfaz de chat en Streamlit`
  - `docs: README con arquitectura e instrucciones`
  - `docs: ejemplos de preguntas y respuestas`
  - `chore: preparación para deploy en Streamlit Cloud`
- Subir todo, incluyendo `inventario.xlsx` (el dataset es público de igual forma).

### 3. Deploy en Streamlit Community Cloud (crítico)
- Conectar el repo en https://share.streamlit.io
- Configurar el entry point como `app/app.py`.
- En la sección **Secrets** del deploy (NO en el código ni en el repo), agregar:
  ```
  GOOGLE_API_KEY = "la_key_real"
  ```
- Confirmar que la app carga y responde en producción, no solo local.
- Tomar una captura de pantalla de la app funcionando y guardarla en `assets/deploy-screenshot.png`.
- Actualizar en `README.md` el enlace real de la app desplegada en la sección "Evidencia del Deploy".

### 4. Revisión final del README (importante, no bloqueante)
- Confirmar que todas las secciones pedidas por el challenge están presentes: descripción general, arquitectura, tecnologías, instrucciones de ejecución, ejemplos de preguntas, ejemplos de respuestas, evidencia de deploy.
- Reemplazar cualquier placeholder tipo `<tu-usuario>` o `[agregar...]` con datos reales.

## Restricciones importantes
- No agregues LangGraph, n8n, ni orquestación multiagente — no aplica al alcance del challenge y no hay tiempo.
- No inviertas tiempo en rediseñar la interfaz visual; la interfaz de chat de Streamlit ya cumple el requisito.
- Si `create_pandas_dataframe_agent` da problemas de compatibilidad de versiones, la alternativa aceptable es usar `langchain.agents.create_pandas_dataframe_agent` (import legacy) — probar ambos si uno falla.
- Usa `gemini-1.5-flash` (capa gratuita) salvo que yo indique lo contrario.

## Definición de "terminado"
- [ ] App corre localmente sin errores
- [ ] App desplegada públicamente y accesible por enlace
- [ ] Captura del deploy guardada en `assets/`
- [ ] README completo sin placeholders pendientes
- [ ] `docs/ejemplos.md` con respuestas reales
- [ ] Repositorio en GitHub, público, con historial de commits claro
- [ ] `.env` real NO está en el repo (solo `.env.example`)
