import streamlit as st
import pandas as pd
import numpy as np

st.title('Microdrip Calculator')

st.write('This app calculates the different variables for a microdrip system')

st.markdown('## Home')
st.sidebar.markdown('## Home')

# st.write('Calculate the flow rate in liters per hour')
# barrel_tap_diameter = st.number_input('Barrel tap diameter (cm)', min_value=0.0, value=0.0)
# barrel_tap_diameter = barrel_tap_diameter / 100
# barrel_tap_flow_rate = (barrel_pressure * np.pi * (barrel_tap_diameter**2)) / 4

# st.write('The flow rate is', barrel_tap_flow_rate, 'liters per hour')