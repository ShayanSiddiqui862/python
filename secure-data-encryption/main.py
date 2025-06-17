from cryptography.fernet import Fernet
import hashlib
import streamlit as st
KEY = Fernet.generate_key()
cipher = Fernet(KEY)
stored_attempts = {}
failed_attempts = 0

# Function to generate a key from a password
def generate_key(password: str) -> bytes:
    # Hash the password to create a key
    key = hashlib.sha256(password.encode()).digest()
    return key