import streamlit as st
from utils.storage import load_users_from_json

st.set_page_config(page_title="Genetic Dating App", page_icon="💘")

# Inisialisasi data
if "users" not in st.session_state:
    load_users_from_json()

st.title("💘 Genetic Dating App")
st.sidebar.title("Menu Navigasi")
st.sidebar.info("Gunakan menu di kiri untuk memilih halaman.")

st.write("Selamat datang di aplikasi dating berbasis algoritma genetika! 🚀")
st.write("Pilih menu **Register**, **Match**, atau **Users List** di sidebar.")
