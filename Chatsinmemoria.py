import os
import time
import warnings
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

warnings.filterwarnings("ignore")

# ============================
# Cargar variables de entorno
# ============================
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ No se encontró OPENAI_API_KEY en el archivo .env")

# ============================
# Configuración del modelo
# ============================
llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=api_key,
    model_name="meta-llama/llama-3.3-70b-instruct",
    temperature=0.9,
)

# ============================
# Prompt del sistema
# ============================
Meta_prompt = """
"""

# ============================
# Chat SIN memoria
# ============================
print("💬 Chatbot vía OpenRouter (SIN memoria)")
print("Escribe 'salir' para terminar.\n")

while True:

    user_input = input("👤 Tú: ").strip()

    if user_input.lower() in ["salir", "exit", "quit"]:
        print("👋 Hasta luego.")
        break

    try:

        # Cada consulta es completamente independiente.
        # El modelo NO recibe conversaciones anteriores.
        messages = []

        if Meta_prompt.strip():
            messages.append(SystemMessage(content=Meta_prompt))

        messages.append(HumanMessage(content=user_input))

        response = llm.invoke(messages)

        print(f"\n🤖 Bot: {response.content.strip()}\n")

        time.sleep(2)

    except Exception as e:
        print(f"\n❌ Error: {e}\n")