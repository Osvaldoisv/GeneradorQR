import qrcode
import streamlit as st

filename = "qr_codes/qr_code.png"

def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=
    )