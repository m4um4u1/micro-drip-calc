import streamlit as st
import pandas as pd
import numpy as np

st.markdown('## Flow from barrel')
st.sidebar.markdown('## Flow from barrel')

st.write('Calculate the flow rate from the barrel through the tap in liters per minute')
barrel_diameter = st.number_input('Barrel diameter (cm)', min_value=0.0, value=1.0)
barrel_height = st.number_input('Water height from tap to top (cm)', min_value=0.0, value=1.0)
barrel_tap_diameter = st.number_input('Barrel tap diameter (cm)', min_value=0.0, value=1.0)


bd_meter = barrel_diameter / 100
btd_meter = barrel_tap_diameter / 100
bh_meter = barrel_height / 100

bd_square_meter = np.pi * ((bd_meter/2)**2)
btd_square_meter = np.pi * ((btd_meter/2)**2)

barrel_tap_flow_rate = (btd_square_meter / bd_square_meter) * np.sqrt(2 * 9.81 * bh_meter)

st.write('The flow speed is', barrel_tap_flow_rate, 'm/s')

btfr_liter_per_minute = barrel_tap_flow_rate * btd_square_meter * 60 * 1000

st.write('The flow rate is', btfr_liter_per_minute, 'liters per minute')

st.write('or', btfr_liter_per_minute * 1000, 'ml per minute')
