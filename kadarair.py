import streamlit as st

import numpy as np

st.write("Perhitungan Kadar Air Sampel") 


Bobot_awal_sampel = st.number_input("Masukkan bobot awal sampel (g) - ") 
Bobot_konstan_sampel = st.number_input("Masukkan bobot konstan (g)")


tombol=st.button("Hitung Kadar air sampel")
if tombol:
    Bobot_awal_sampel = ((Bobot_awal_sampel - Bobot_konstan_sampel/bobot_awal_sampel)*100)
    st.success("persentase kadar air sampel (%) sebesar... {round (kadar air sampel)}")

    st.balloons()