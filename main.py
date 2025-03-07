import re
import streamlit as st

# page styling for the default settings
st.set_page_config("Password Strength Checker By M.Sameer Awan", page_icon="🌘", layout="centered")
# Custom Css
st.markdown(
    """
    <style>
    .main {text-align:center}
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px; }
    .stButton button:hover {background-color: #45a049;}
    </style>
    """, unsafe_allow_html=True)

# Page Title and Description
st.title("Password Strength Checker 🔐", layout="centered")
st.write("Enter your password below to check your passwords strength 🔍", layout="centered")

# Function to check the password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **Both uppercase and lower case letter**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("�� Password should contain **at least one digit (0-9) **.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one special character (!@#$%^&*(),.?\":{}|<>)**.")

    # Display Password's Strength results
    if score == 4:
        st.success("✅ Your Password is **Very Strong**.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - you should impore password by adding more features.")
    else:
        st.error("❌ Your Password is **Very Weak**. ")

    # Display Feedback
    if feedback:
        with st.expander("🔍 **Impore Your Password**"):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter your Password:", type="password", layout="centered", help="Ensure that your password is strong 🔐")
# Button Workflow
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
