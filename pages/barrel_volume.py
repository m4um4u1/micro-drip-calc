import streamlit as st
import numpy as np

st.markdown('## Volumen eines Fasses berechnen')
st.sidebar.markdown('## Volumen eines Fasses berechnen')

# Barrel dimensions and volume
st.write('Gib die Abmessungen des Fasses ein')
barrel_width_upper = st.number_input(
    'Diameter oben und unten (cm)', min_value=0.0, value=60.0)
barrel_width_middel = st.number_input(
    'Diameter in der Mitte (cm)', min_value=0.0, value=70.0)
barrel_height = st.number_input(
    'Höhe (cm)', min_value=0.0, value=80.0)

# Convert to meters
barrel_width_upper = barrel_width_upper / 100
barrel_width_middel = barrel_width_middel / 100
barrel_height = barrel_height / 100


# Calculate the barrel volume in liters
barrel_volume = (np.pi * barrel_height * ((barrel_width_middel **
                 2)/2 + (barrel_width_upper**2)/4)) / 3 * 1000

st.write('Das Volumen des Fasses beträgt ca.', barrel_volume, 'liter')
