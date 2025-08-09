import streamlit as st

st.subheader("👥 Daftar Semua Pengguna")
for user in st.session_state.users:
    st.write(f"**{user['name']}**, {user['age']} tahun, {user['gender']} dari {user['location']}")
    st.write(f"Minat: {user['interest']}")
    st.markdown("---")
