import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

load_dotenv()

st.set_page_config(page_title="Agente Inteligente - Mercado Central 24h", page_icon="🛒")
st.title("🛒 Agente Inteligente - Mercado Central 24h")
st.caption("Hazme preguntas en lenguaje natural sobre el inventario del supermercado.")

# --- Carga defensiva de la API Key ---
# Prioridad: variable de entorno / secrets de Streamlit > input manual
api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY", None) if hasattr(st, "secrets") else os.getenv("GOOGLE_API_KEY")

if not api_key:
    api_key = st.text_input("Ingresa tu Google API Key (Gemini)", type="password")

if not api_key:
    st.info("Necesitas una API Key de Gemini para continuar. Consíguela gratis en https://aistudio.google.com/apikey")
    st.stop()

# --- Carga del dataset ---
DATA_PATH = os.path.join(os.path.dirname(__file__), "inventario.xlsx")

@st.cache_data
def load_data(path):
    if path.endswith(".xlsx"):
        df = pd.read_excel(path)
    else:
        df = pd.read_csv(path)
    for col in df.columns:
        if "vencimiento" in col.lower():
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df

if not os.path.exists(DATA_PATH):
    st.error(f"No se encontró el archivo de datos en: {DATA_PATH}. Súbelo a la carpeta 'app/' con el nombre 'inventario.xlsx'.")
    st.stop()

df = load_data(DATA_PATH)

with st.expander("Ver muestra del dataset"):
    st.dataframe(df.head(10))

# --- Construcción del agente con modelos Gemini 3.x vigentes ---
MODELOS_CANDIDATOS = [
    "gemini-3.5-flash-lite",  # más rápido y económico, ideal para capa gratuita
    "gemini-3.6-flash",       # más nuevo, más capaz
    "gemini-2.5-flash-lite",  # respaldo adicional
]

@st.cache_resource
def get_agent(_df, _api_key):
    llm = None
    for modelo in MODELOS_CANDIDATOS:
        try:
            cand = ChatGoogleGenerativeAI(
                model=modelo,
                api_key=_api_key,
                temperature=0,
            )
            cand.invoke("test")
            llm = cand
            break
        except Exception:
            continue
    if not llm:
        llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", api_key=_api_key, temperature=0)

    return create_pandas_dataframe_agent(
        llm,
        _df,
        verbose=True,
        allow_dangerous_code=True,
        agent_type="tool-calling",
        prefix="Eres un asistente inteligente experto en gestión de inventarios para el supermercado Mercado Central 24h. Responde siempre en español de forma clara, directa y concisa a partir del dataframe de pandas proporcionado.",
    )

agent = get_agent(df, api_key)

# --- Historial de chat ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pregunta = st.chat_input("Escribe tu pregunta sobre el inventario...")

if pregunta:
    st.session_state.messages.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                respuesta = agent.invoke({"input": pregunta})
                salida = respuesta["output"] if isinstance(respuesta, dict) else str(respuesta)
            except Exception as e:
                salida = f"Ocurrió un error al procesar la pregunta: {e}"
            st.markdown(salida)

    st.session_state.messages.append({"role": "assistant", "content": salida})
