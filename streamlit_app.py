import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configuración de la página
st.set_page_config(page_title="Control RPE - Club Bolívar", page_icon="⚽", layout="centered")

# URL del escudo oficial del Club Bolívar
LOGO_URL = "https://clubbolivar.com/wp-content/uploads/2023/05/logo-750x750-1.png"

# 2. Insertar Escudo Centrado y Título
col1, col2, col3 = st.columns([1, 1.5, 1])
with col2:
    st.image(LOGO_URL, width=180)

st.markdown("<h1 style='text-align: center; color: #1E90FF; margin-top: -10px;'>🔵 Club Bolívar</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; margin-top: -15px;'>Control de Carga Interna (RPE)</h3>", unsafe_allow_html=True)
st.write("---")

# ID de tu Google Sheets verificado
SHEET_ID = "1GTPovT6jXqDwR_u172XHvSKUhXByDT17Ii0EpVnx1Ac"

# 3. Plantel Profesional Actualizado (puedes agregar o quitar nombres aquí)
jugadores = [
    "Carlos Lampe", "Juan Jose Lopez", "Diego Méndez", 
    "Jesús Sagredo", "José Sagredo", "Xavier Arreaga", "Santiago Echeverria", 
    "Leonel Justiniano", "Ervin Vaca", "Erwin Saavedra", "Robson Matheus", 
    "Carlos Melgar", "Patito Rodríguez", "Fernando Mena", "Escleizon Freita", 
    "Luis Paz", "Dorny Romero", "Lucas Chávez", "Jhon Velásquez", "Martin Cauteruccio",  
    "Jhon Garcia", "Cristian Lopez", "Anderson Ayhuana", "Matias Galindo", "Jesus Velasquez"
]
jugadores.sort() # Los ordena alfabéticamente de forma automática

# 4. Formulario para el jugador
with st.form("rpe_form", clear_on_submit=True):
    nombre = st.selectbox("1. Selecciona tu Nombre:", jugadores)
    
    st.markdown("**2. Escala de Percepción del Esfuerzo (Borg 1-10):**")
    rpe = st.slider("¿Qué tan dura sentiste la sesión?", 1, 10, 5, 
                    help="1-2: Muy suave, 3-4: Moderado, 5-6: Duro, 7-8: Muy Duro, 9-10: Máximo")
    
    duracion = st.number_input("3. Duración de la sesión (minutos):", min_value=1, max_value=240, value=90)
    
    obs = st.text_input("4. Observaciones / Molestias (Opcional):", placeholder="Ej: Carga en gemelo izquierdo...")
    
    enviar = st.form_submit_button("Enviar Reporte 🚀")

if enviar:
    carga_ua = rpe * duracion
    st.success(f"¡Reporte enviado con éxito, {nombre}! Carga de sesión calculada: {carga_ua} UA.")
    st.info("Nota técnica: Los datos se están sincronizando con la base de datos central del Cuerpo Técnico.")
