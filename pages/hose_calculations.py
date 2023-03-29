import streamlit as st
import pandas as pd
import numpy as np

st.markdown('## Schlauchberechnungen')
st.sidebar.markdown('## Schlauchberechnungen')

st.markdown('### Druckverluste')
st.write('Berechne die Druckverluste in einem Schlauch mit verschiedenen Durchmessern und Längen')

# Pipe dimensions
st.write('Gib die Schlauchdurchmesser und Längen ein')
pipe_diameter = st.number_input('Schlauchdurchmesser (mm)', min_value=0.0, value=13.0)
pipe_length = st.number_input('Schlauchlänge (m)', min_value=0.0, value=10.0)
flow_speed = st.number_input('Strömungsgeschwindigkeit (m/s)', min_value=0.0, value=1.0)

# Convert to meters
pipe_diameter = pipe_diameter / 1000

# Calculate the loss of pressure in the pipe
pipe_pressure_loss = (0.03 * pipe_length * 1000 * flow_speed) / (pipe_diameter * 2)

# Convert to Bar
pipe_pressure_loss = pipe_pressure_loss / 100000
st.write('Der Druckverlust im Schlauch ist', pipe_pressure_loss, 'Bar')

st.markdown('### Microdrip Lochung')
st.write('Berechne die Lochung für Microdrip Schläuche')

# Pipe dimensions
st.write('Gib die Länge vom Schlauch ein und wie viele Löcher pro Meter')
st.write('Die Länge wird von oben übernommen')

holes_per_meter = st.number_input('Löcher pro Meter', min_value=0.0, value=10.0)

# Calculate the space between the holes in the pipe
hole_spacing = pipe_length / holes_per_meter

# Convert to cm
hole_spacing = hole_spacing * 100

st.write('Der Abstand zwischen den Löchern sollte', hole_spacing, 'cm haben')


