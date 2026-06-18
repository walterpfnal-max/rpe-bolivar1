import streamlit as st
import pandas as pd
from datetime import datetime

import gspread
from google.oauth2.service_account import Credentials

# ID de tu Google Sheets verificado
SHEET_ID = "1GTPovT6jxQdWr_u172XHvSKUhXByDT17Ii0EpVnx1Ac"

# Configuración de la página
st.set_page_config(page_title="Control RPE - Club Bolívar", page_icon="⚽", layout="centered")

# URL del escudo oficial del Club Bolívar
LOGO_URL = "https://clubbolivar.com/wp-content/uploads/2023/05/logo-750x750-1.png"

col1, col2, col3 = st.columns([1, 1.5, 1])
with col2:
    st.image(LOGO_URL, width=180)

st.markdown("<h1 style='text-align: center; color: #1E90FF; margin-top: -10px;'>⚽ Club Bolívar</h1>", unsafe_html=True)
st.markdown("<h3 style='text-align: center; margin-top: -15px;'>Control de Carga Interna (RPE)</h3>", unsafe_html=True)
st.write("---")

# Plantel Profesional Actualizado
jugadores = [
    "Carlos Lampe", "Juan Jose Lopez", "Diego Méndez",
    "Jesús Sagredo", "José Sagredo", "Xavier Arreaga", "Santiago Echeverria",
    "Leonel Justiniano", "Ervin Vaca", "Erwin Saavedra", "Robson Matheus"
]

# Formulario en la App
nombre = st.selectbox("1. Selecciona tu Nombre:", jugadores)
rpe = st.slider("2. Escala de Percepción del Esfuerzo (Borg 1-10):", 1, 10, 5)
duracion = st.number_input("3. Duración de la sesión (minutos):", min_value=1, max_value=240, value=90, step=5)
observaciones = st.text_input("4. Observaciones / Molestias (Opcional):", placeholder="Ej: Carga en gemelo izquierdo...")

if st.button("Enviar Reporte 🚀"):
    carga_ua = rpe * duracion
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # Autenticación con Google usando los Secrets de Streamlit
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scopes)
        client = gspread.authorize(creds)
        
        # Conexión directa a tu documento y a la pestaña "Hoja 1"
        sheet = client.open_by_key(SHEET_ID).worksheet("Hoja 1")
        
        # Guardar la nueva fila de datos
        nueva_fila = [fecha_actual, nombre, rpe, duracion, carga_ua, observaciones]
        sheet.append_row(nueva_fila)
        
        st.success(f"¡Reporte enviado con éxito, {nombre}! Carga de sesión calculada: {carga_ua} UA.")
        st.info("Nota técnica: Los datos se han sincronizado automáticamente con la base de datos central.")
    except Exception as e:
        st.error(f"Error al conectar con Google Sheets: {e}")
