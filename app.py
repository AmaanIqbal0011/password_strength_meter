import streamlit as st
import re


st.set_page_config(page_title="Password Strength Checker")

st.title("Password Strength Meter")
st.markdown("""
## Welcome to the Password strength Checker
use this tool to check the strength of your password and get tips on how to make it stronger""")

password = st.text_input("Enter your Password", type="password")
check = st.button("Check Button")

feedback = []

score = 0

if check and  password:
    if len(password) >= 8 :
        score += 1
    else : 
        feedback.append("❌password must be atleast 8 Character long") 
        
    if re.search(r'[A-Z]',password) :
        score += 1  
    else : 
        feedback.append("❌password should contain atleast 1 uppercase letter") 
        
    if re.search(r'[a-z]',password) :
        score += 1  
    else : 
        feedback.append("❌password should contain atleast 1 lowercase letter")
        
    if re.search(r'\d',password):
        score += 1  
    else : 
        feedback.append("❌password should contain atleast 1 digit")
        
    if re.search(r'[!@#$%^&*()_+\-={}\[\]:;?]', password):
        score += 1  
    else : 
        feedback.append("❌password should contain atleast 1 special Character") 
        
    if score == 5 :
        feedback.append("🟢Your Password is Strong") 
    elif score == 4 :
        feedback.append("🟠Your password is medium strength.It could be stronger.")
    elif score == 3:
         feedback.append("🟡Your password need to be stronger.")   
    else : 
        feedback.append("🔴Your Password is weak.Make it stronger.")   
        
        
    if feedback : 
        st.markdown("Suggestion to make Your Password Strong") 
        for tip in feedback:
            st.write(tip)
            
elif check and not password : 
    "please enter your password to get Started"                                          