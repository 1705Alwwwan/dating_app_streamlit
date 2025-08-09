import streamlit as st
from utils.storage import save_users_to_json

st.subheader("📝 Daftar Pengguna Baru")
name = st.text_input("Nama")
gender = st.radio("Jenis Kelamin", ["male", "female"], horizontal=True)
age = st.slider("Usia", 18, 60, 25)
location = st.text_input("Lokasi (Contoh: Jakarta)")
interest = st.text_area("Minat (pisahkan dengan koma)", "musik, film, coding")

if st.button("Simpan"):
    user = {
        "name": name,
        "gender": gender,
        "age": age,
        "location": location,
        "interest": interest.lower()
    }
    st.session_state.users.append(user)
    save_users_to_json()
    st.success("Pengguna berhasil ditambahkan!")
