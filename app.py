import streamlit as st
import streamlit.components.v1 as components
import pathlib

st.set_page_config(page_title="Inter | Riesgo Compartido", layout="wide")

html = pathlib.Path("index.html").read_text(encoding="utf-8")

components.html(html, height=2400, scrolling=True)
