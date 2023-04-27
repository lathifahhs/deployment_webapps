import streamlit as st

st.title('aplikasi perhitungan molaritas')

bobot=st.number_input("masukkan nilai bobot")
volume=st.number_input("masukkan nilai volume")
mr=st.number_input("masukkan nilai input")

tombol=st.button("hitung nilai molaritas")

if tombol:
    nilai_molaritas = bobot/(mr*volume)
    st.success(f'nilai molaritas adalah {nilai_molaritas}')
