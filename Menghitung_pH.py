import streamlit as st
import numpy as np

st.title('menghitung kadar pH titrasi :green[Basa kuat oleh Asam kuat]')
M_titrat= st.number_input('masukkan Molaritas titran',step = 0.0001, format = "%.4f", value = 0.1000)
V_titrat= st.number_input('masukkan volume titran',value = 25.00)
M_titran= st.number_input('masukkan Molaritas titrat',step = 0.0001, format = "%.4f", value = 0.1000)
V_titran= st.number_input('masukkan volume titrat',value = 25.00)

mmol_titrat= M_titrat * V_titrat
mmol_titran= M_titran * V_titran
V_total= V_titrat + V_titran

sisa_mol= abs(mmol_titran - mmol_titrat)
Konsentrasi= sisa_mol/V_total

pH = round(-(np.log10(Konsentrasi)),2)
if st.button('tampilkan nilai ph') :
    if mmol_titran > mmol_titrat :
        st.write('nilai pH adalah :',14 - pH)
    elif mmol_titran == mmol_titrat :
        st.write('nilai pH adalah :' , 7)
    else :
        st.write('nilai pH adalah :' ,pH)
else :
    st.write('tekan tombol untuk memunculkan nilai')