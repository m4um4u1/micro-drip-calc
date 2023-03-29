import streamlit as st
import numpy as np

st.markdown('## Strömungsmessung')
st.sidebar.markdown('## Strömungsmessung')

st.write('Berechne die Durchflussmenge mit verschiedenen Messmethoden')

st.markdown('### Volumenstrom')
# Flow from barrel knowing volume and time to drain
st.write('Der Volumenstrom oder Durchflussrate und Durchflussmenge genannt, gibt an, wie viel Volumen eines Mediums pro Zeitspanne durch einen festgelegten Querschnitt transportiert wird.')
st.write('Um den Volumenstrom zu berechnen, muss das Volumen des Fasses und die Zeit bis das Fass leer ist bekannt sein.')

barrel_volume = st.number_input('Fassvolumen (l)', min_value=0.0, value=180.0)
barrel_time_to_drain = st.number_input('Zeit bis das Fass leer ist (min)', min_value=0.0, value=60.0)

# Convert to m3
barrel_volume = barrel_volume / 1000

# Convert time to seconds
barrel_time_to_drain = barrel_time_to_drain * 60

# Calculate the flow from the barrel in m3/h
barrel_volume_flow_qubic = barrel_volume / barrel_time_to_drain 

st.write('Der Volumenstrom aus dem Fass ist', barrel_volume_flow_qubic, 'm3/h')

# Convert to l/min
barrel_volume_flow_liters = barrel_volume_flow_qubic * 1000 * 60

st.write('Der Volumenstrom aus dem Fass ist', barrel_volume_flow_liters, 'l/min')

st.markdown('### Strömungsgeschwindigkeit')

st.write('Berechne die Strömungsgeschwindigkeit, wenn der Volumenstrom und der Durchmesser des Rohres bekannt ist')

tube_diameter = st.number_input('Durchmesser des Rohres (cm)', min_value=0.0, value=1.0)

# Convert to meters
tube_diameter = tube_diameter / 100

# Calculate the flow speed from the barrel 
barrel_flow_speed = (barrel_volume_flow_qubic * 4) / (np.power(tube_diameter, 2) * np.pi)

st.write('Die Strömungsgeschwindigkeit aus dem Fass ist', barrel_flow_speed, 'm/s')

st.markdown('### Massenstrom')

st.write('Der Massenstrom, auch Massendurchsatz, ist die Masse eines Mediums, das sich pro Zeitspanne durch einen Querschnitt bewegt. Aus dem Volumenstrom und der Dichte kann der Massenstrom abgeleitet werden.')
st.write('Der Volumenstrom wird oben berechnet. Die Dichte des Mediums muss hier noch eingegeben werden.')
tube_density = st.number_input('Dichte des Mediums (kg/m3)', min_value=0.0, value=1000.0)

# Calculate the mass flow from the barrel
barrel_mass_flow = barrel_volume_flow_qubic * tube_density

st.write('Der Massenstrom aus dem Fass ist', barrel_mass_flow, 'kg/s')