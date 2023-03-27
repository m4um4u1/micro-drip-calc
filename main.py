import streamlit as st
import pandas as pd
import numpy as np

st.title('Microdrip Calculator')

st.write('This app calculates the different variables for a microdrip system')

st.write('Please enter the following variables')

# Input variables
# Barrel dimensions and volume
st.write('Calculate the volume of the barrel in liters (when the barrel is full)')
barrel_width_upper = st.number_input('Barrel width in the top and bottom (cm)', min_value=0.0, value=0.0)
barrel_width_middel = st.number_input('Barrel width in the middel (cm)', min_value=0.0, value=0.0)
barrel_height = st.number_input('Barrel height (cm)', min_value=0.0, value=0.0)

# Calculate the barrel volume in liters 
barrel_volume = (np.pi * barrel_height * ((barrel_width_middel**2)/2 + (barrel_width_upper**2)/4)) / 3 / 1000

st.write('The volume of the barrel is', barrel_volume, 'liters')

st.write('Calculate the pressure in the barrel in bar, using water as the working fluid and gravity as the force')
fluid_density = st.number_input('Fluid density (kg/m3) - water has a density of 1000 kg/m3', min_value=0.0, value=1000.0)
barrel_tap_height = st.number_input('Barrel tap height (cm)', min_value=0.0, value=0.0)
# Calculate from where the pressure is calculated in meters
barrel_height_tap = barrel_height - barrel_tap_height / 100
barrel_pressure = (fluid_density * 9.81 * barrel_height_tap) / 100000

st.write('The pressure in the barrel is', barrel_pressure, 'bar')