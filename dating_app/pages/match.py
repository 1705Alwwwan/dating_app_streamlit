import streamlit as st
from utils.encoding import encode_interests
from utils.genetic import match_user

st.subheader("❤️ Temukan Pasangan yang Cocok")

if not st.session_state.users:
    st.warning("Belum ada pengguna yang terdaftar.")
else:
    names = [user["name"] for user in st.session_state.users]
    current_name = st.selectbox("Pilih Nama Anda", names)

    interests = [u["interest"] for u in st.session_state.users]
    encoded_vectors, vectorizer = encode_interests(interests)

    for i, user in enumerate(st.session_state.users):
        user["vector"] = encoded_vectors[i]

    current_user = next(u for u in st.session_state.users if u["name"] == current_name)
    candidates = [u for u in st.session_state.users if u["name"] != current_name]

    match = match_user(current_user, candidates)
    if match:
        st.success(f"Pasangan paling cocok untuk {current_user['name']}: **{match['name']}** 💖")
        st.write(f"Jenis Kelamin: {match['gender']}")
        st.write(f"Usia: {match['age']}")
        st.write(f"Lokasi: {match['location']}")
        st.write(f"Minat: {match['interest']}")
    else:
        st.info("Tidak ditemukan pasangan yang cocok.")
