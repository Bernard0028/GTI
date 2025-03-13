import json
import streamlit as st
from streamlit_lottie import st_lottie

# Load Lottie Animation from Local JSON File
def load_lottie_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_animation = load_lottie_file("lottie_terror.json")

if 'page' in locals() and page == "Overview":
    st_lottie(lottie_animation, height=250, key="terrorism_lottie")
