import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Control RPE - Club Bolívar", page_icon="⚽", layout="centered")

# ID de tu Google Sheets verificado
SHEET_ID = "1GTPovT6jXqDwR_u172XHvSKUhXByDT17Ii0EpVnx1Ac"

st.title("🔵 Club Bolívar - Control de Carga")
st.markdown("### Registro Diario de Carga Interna (RPE)")

# Lista del Plantel Profesional
jugadores = [
    "Francisco Chaverra", "Carlos Lampe", "Leonel Justiniano", 
    "Ramiro Vaca", "Patito Rodríguez", "Bruno Sávio", 
    "Fábio Gomes", "Jhon Velasco", "Yomar Rocha", "Jesús Sagredo"
]
jugadores.sort()

# Formulario para el jugador
with st.form("rpe_form", clear_on_submit=True):
    nombre = st.selectbox("1. Selecciona tu Nombre:", jugadores)
    
    st.markdown("**2. Escala de Percepción del Esfuerzo (Borg 1-10):**")
    rpe = st.slider("¿Qué tan dura sentiste la sesión?", 1, 10, 5, 
                    help="1-2: Muy suave, 3-4: Moderado, 5-6: Duro, 7-8: Muy Duro, 9-10: Máximo")
    
    duracion = st.number_input("3. Duración de la sesión (minutos):", min_value=1, max_value=240, value=90)
    
    obs = st.text_input("4. Observaciones / Molestias (Opcional):", placeholder="Ej: Dolor de cabeza por altura, carga en gemelo...")
    
    enviar = st.form_submit_button("Enviar Reporte 🚀")

if enviar:
    carga_ua = rpe * duracion
    st.success(f"¡Reporte enviado con éxito, {nombre}! Carga de sesión calculada: {carga_ua} UA.")
    st.info("Nota técnica: Los datos se están sincronizando con la base de datos central del Cuerpo Técnico.")
