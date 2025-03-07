import re
import streamlit as st
import random
import string

def check_password_strength(password):
    score = 0
    st.session_state['password'] = password
    
    # Length Check
    if len(password) >= 8:
        score += 1
        st.write("✅ Password must be at least 8 characters long.")
    else:
        st.write("❌ Password must be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
        st.write("✅ Include both uppercase and lowercase letters.")
    else:
        st.write("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
        st.write("✅ Include at least one number (0-9).")
    else:
        st.write("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*<>/'|+=`]", password):
        score += 1
        st.write("✅ Include at least one special character ")
    else:
        st.write("❌ Include at least one special character (!@#$%^&*).")
    
    
    if score == 4:
        st.write("✅ Strong Password - Good to go!")
        st.page_link("pages/success.py", label="Submit")
    elif score == 3:
        st.write("🟡MeduimPassword-Can be improved")
    else:
        st.write("❌ Weak Password - Improve it using the suggestions above.")


def is_common_password(password):
    common_passwords = ["password123", "123456", "qwerty", "letmein", "password", "12345"]
    if password in common_passwords:
       st.error("❌ Common Password - Please choose a different password.")
       return True
    return False


st.title("Password Strength Checker")
password = st.text_input("Enter a password:")
if password:
    if not is_common_password(password):
        
        check_password_strength(password)
        
        
        

if st.button("Generate Strong Password"):
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_lowercase , k=12))
    st.success(f"Generated Strong Password: {password}")
    