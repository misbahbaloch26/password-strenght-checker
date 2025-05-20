import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, lowercase_error, uppercase_error, digit_error, special_char_error]
    score = 5 - sum(errors)

    if score == 5:
        return "Strong 💪", "green"
    elif score >= 3:
        return "Moderate ⚠️", "orange"
    else:
        return "Weak ❌", "red"

# Streamlit UI
st.title("🔐 Password Strength Checker")
password_input = st.text_input("Enter your password", type="password")

if password_input:
    strength, color = check_password_strength(password_input)
    st.markdown(f"<h4 style='color:{color}'>{strength}</h4>", unsafe_allow_html=True)

    st.write("### Checklist:")
    st.markdown("- ✅ At least 8 characters" if len(password_input) >= 8 else "- ❌ Less than 8 characters")
    st.markdown("- ✅ Contains a lowercase letter" if re.search(r"[a-z]", password_input) else "- ❌ No lowercase letter")
    st.markdown("- ✅ Contains an uppercase letter" if re.search(r"[A-Z]", password_input) else "- ❌ No uppercase letter")
    st.markdown("- ✅ Contains a number" if re.search(r"\d", password_input) else "- ❌ No number")
    st.markdown("- ✅ Contains a special character" if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password_input) else "- ❌ No special character")
