import streamlit as st
import pandas as pd
import numpy as np

st.markdown('## Barrel pressure')
st.sidebar.markdown('## Barrel pressure')

st.write('Calculate the pressure in the barrel in bar, using water as the working fluid and gravity as the force')
fluid_density = st.number_input('Fluid density (kg/m3) - water has a density of 1000 kg/m3', min_value=0.0, value=1000.0)
barrel_height = st.number_input('Barrel/waterlevel height (cm)', min_value=0.0, value=90.0)
barrel_tap_height = st.number_input('Barrel tap height (cm)', min_value=0.0, value=15.0)

# Calculate from where the pressure is calculated in meters
calc_height = (barrel_height - barrel_tap_height)
st.write('The pressure is calculated from', calc_height, 'cm from the top of the barrel')
barrel_pressure = (fluid_density * 9.81 * (calc_height / 100)) / 100000

st.write('The pressure in the barrel is', barrel_pressure, 'bar when the barrel is full')

st.write('Calculate the change in pressure in the barrel in bar with different water levels in height')
# Create a dataframe with the hours and the pressure in the barrel in bar with different water levels in height

barrel_water_levels = pd.DataFrame({'Water level over tap (cm)': np.arange(5, calc_height + 1, 5)})
barrel_water_levels['Pressure (bar)'] = (fluid_density * 9.81 * (barrel_water_levels['Water level over tap (cm)'] / 100)) / 100000

st.write(barrel_water_levels)

# Create a plot of the pressure in the barrel in bar with different water levels in height
st.line_chart(data=barrel_water_levels, x='Water level over tap (cm)', y='Pressure (bar)')






