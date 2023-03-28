import streamlit as st
import numpy as np

st.markdown('## Barrel volume')
st.sidebar.markdown('## Barrel volume')

# Barrel dimensions and volume
st.write('Calculate the volume of the barrel in liters (when the barrel is full)')
barrel_width_upper = st.number_input(
    'Barrel width in the top and bottom (cm)', min_value=0.0, value=60.0)
barrel_width_middel = st.number_input(
    'Barrel width in the middel (cm)', min_value=0.0, value=70.0)
barrel_height = st.number_input(
    'Barrel height (cm)', min_value=0.0, value=80.0)

# Convert to meters
barrel_width_upper = barrel_width_upper / 100
barrel_width_middel = barrel_width_middel / 100
barrel_height = barrel_height / 100


# Calculate the barrel volume in liters
barrel_volume = (np.pi * barrel_height * ((barrel_width_middel **
                 2)/2 + (barrel_width_upper**2)/4)) / 3 * 1000

st.write('The volume of the barrel is', barrel_volume, 'liters')
