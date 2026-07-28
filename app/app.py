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

DATA_PATH = os.path.join(os.path.dirname(__file__), "inventario.xlsx")

@st.cache_data
def load_data(path):
    return pd.read_excel(path)

if not os.path.exists(DATA_PATH):
    st.error(f"No se encontró el archivo de datos en: {DATA_PATH}.")
    st.stop()

df = load_data(DATA_PATH)

with st.expander("Ver muestra del dataset"):
    st.dataframe(df.head(10))

api_key = os.getenv("GOOGLE_API_KEY")

@st.cache_resource
def get_agent(_df, _api_key):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=_api_key,
        temperature=0,
    )
    return create_pandas_dataframe_agent(
        llm,
        _df,
        verbose=True,
        allow_dangerous_code=True,
        agent_type="tool-calling",
    )

agent = get_agent(df, api_key)

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
