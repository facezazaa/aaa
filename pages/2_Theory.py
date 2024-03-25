import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url) 
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/b8140f0c-c590-4472-bc9b-95ae27d7ab83/mdPq45E3hl.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello, key="hello")

st.header("ทฤษฎีที่เกี่ยวข้อง")

st.subheader("1.ทฤษฎีเหมืองข้อมูล")
st.info("""
อธิบายว่าทฤษฎีเหมืองข้อมูลช่วยค้นหาความรู้และข้อมูลเชิงลึกจากข้อมูลขนาดใหญ่
""")
st.subheader("2.เทคนิคการจินตทัศน์ข้อมูลวิเคราะห์ถดถอยเชิงเส้น(Linear Regression)")
st.info("""
อธิบายเทคนิคที่ใช้กันทั่วไป เช่น แผนภูมิกระจาย เส้นแนวโน้ม กราฟเส้น
""")
