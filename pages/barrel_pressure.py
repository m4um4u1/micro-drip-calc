import streamlit as st
import pandas as pd
import numpy as np

st.markdown('## Druck in einem Fass berechnen')
st.sidebar.markdown('## Druck in einem Fass berechnen')

st.write('Berechne den Druck in einem Fass mit verschiedenen Füllständen und dem Wasserstand über dem Auslauf')
fluid_density = st.number_input(
    'Dichte der Flüssigkeit (kg/m3) - Wasser hat eine Dichte von 1000 kg/m3', min_value=0.0, value=1000.0)
barrel_height = st.number_input(
    'Wasser/Fasshöhe (cm)', min_value=0.0, value=90.0)
barrel_tap_height = st.number_input(
    'Ventilhöhe (cm)', min_value=0.0, value=15.0)

# Calculate from where the pressure is calculated in meters
calc_height = (barrel_height - barrel_tap_height)
st.write('Der Druck wird bis',
         calc_height, 'cm höhe berechnet')
barrel_pressure = (fluid_density * 9.81 * (calc_height / 100)) / 100000

st.write('Der Druck in dem Fass ist',
         barrel_pressure, 'bar wenn das Fass voll ist')

st.write('Hier siehst du die Druckverteilung von einem Fass mit verschiedenen Füllständen und dem Wasserstand über dem Auslauf')
# Create a dataframe with the hours and the pressure in the barrel in bar with different water levels in height

barrel_water_levels = pd.DataFrame(
    {'Wasserstand über den Auslauf (cm)': np.arange(5, calc_height + 1, 5)})
barrel_water_levels['Druck (bar)'] = (
    fluid_density * 9.81 * (barrel_water_levels['Wasserstand über den Auslauf (cm)'] / 100)) / 100000

# reverse the dataframe
barrel_water_levels = barrel_water_levels.iloc[::-1]

st.write(barrel_water_levels)

# Create a plot of the pressure in the barrel in bar with different water levels in height
st.line_chart(data=barrel_water_levels,
              x='Wasserstand über den Auslauf (cm)', y='Druck (bar)')