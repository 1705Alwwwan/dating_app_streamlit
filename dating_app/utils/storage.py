import json
import os
import streamlit as st

DATA_FILE = "data/users.json"

def save_users_to_json():
    with open(DATA_FILE, "w") as f:
        json.dump(st.session_state.users, f, indent=2)

def load_users_from_json():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            st.session_state.users = json.load(f)
    else:
        st.session_state.users = []
