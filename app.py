import streamlit as st
from google import genai
import os
import re
from dotenv import load_dotenv

# Cargar la llave secreta desde el archivo .env
load_dotenv()

# Inicializar el cliente nuevo de Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def detect_provider(tf_code):
    """Detecta si el código original es de AWS, Azure o GCP."""
    if re.search(r'provider\s+"azurerm"', tf_code):
        return "Azure"
    elif re.search(r'provider\s+"aws"', tf_code):
        return "AWS"
    elif re.search(r'provider\s+"google"', tf_code):
        return "GCP"
    return "Desconocido"

def translate_terraform(code, source, target):
    """Manda el prompt a Gemini para traducir el código usando el SDK nuevo."""
    prompt = f"""
    Eres un ingeniero experto en DevOps, SRE y Terraform. 
    Convierte el siguiente código de Terraform que está hecho para {source} y tradúcelo para que funcione en {target}.
    Aplica las mejores prácticas de {target}.
    Devuelve ÚNICAMENTE el código válido de Terraform, sin explicaciones ni saludos.
    
    Código original:
    {code}
    """
    # Llamada con la nueva sintaxis de google-genai
    response = client.models.generate_content(
        model='gemini-3.1-flash-lite-preview',
        contents=prompt,
    )
    return response.text.replace('```hcl', '').replace('```terraform', '').replace('```', '').strip()

# --- INTERFAZ GRÁFICA CON STREAMLIT ---
st.set_page_config(page_title="AI Terraform Translator", page_icon="🏗️", layout="wide")

st.title("🏗️ AI-Powered Terraform Cloud Translator")
st.markdown("Sube tu archivo `.tf`, el sistema detectará el proveedor y Gemini lo traducirá a tu nube destino.")

uploaded_file = st.file_uploader("Sube tu archivo de Terraform (.tf)", type=["tf"])

if uploaded_file is not None:
    # Leer el código subido
    tf_code = uploaded_file.getvalue().decode("utf-8")
    
    # Detectar proveedor automáticamente
    source_cloud = detect_provider(tf_code)
    st.info(f"☁️ **Proveedor original detectado:** {source_cloud}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Código Original")
        st.code(tf_code, language="hcl")
        
    with col2:
        st.subheader("Traducción a Nube Destino")
        target_cloud = st.selectbox("Selecciona la nube a la que quieres migrar:", ["AWS", "Azure", "GCP"])
        
        if st.button("🚀 Traducir con Gemini AI"):
            if source_cloud == target_cloud:
                st.warning("El proveedor de origen y destino son el mismo.")
            else:
                with st.spinner("Gemini está traduciendo la infraestructura..."):
                    translated_code = translate_terraform(tf_code, source_cloud, target_cloud)
                    st.code(translated_code, language="hcl")
                    st.success("¡Traducción completada!")
                    
                    # Botón para descargar el nuevo archivo
                    st.download_button(
                        label="⬇️ Descargar main.tf traducido",
                        data=translated_code,
                        file_name=f"main_{target_cloud.lower()}.tf",
                        mime="text/plain"
                    )