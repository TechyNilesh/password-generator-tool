import streamlit as st
import random
import PIL

lower = "abcdefghijklmnopqrstuvwxyz"
uper = lower.upper()
number = "1234567890"
special = "[]{}()*;/_-"

pass_dict = {"Lower Character":lower,"Upper Character":uper,"Numbers":number,"Special Character":special}

html_temp = """
    <div style="background-color:#010200;padding:6px; margin-bottom: 15px;">
    <h2 style="color:white;text-align:center;">Password Generator</h2>
    <h4 style="color:white;text-align:center;">Design & Developed By Nilesh Verma</h4>
    <center><a href="https://github.com/TechyNilesh/password-generator-tool" target="_blank">Code GitHub Link</a></center>
    </div>
    """    
st.markdown(html_temp, unsafe_allow_html=True)

m_s = st.multiselect('Include Following Character:', ["Lower Character","Upper Character","Numbers","Special Character"])
length = st.number_input('Enter a length of the password you want:',step=1,min_value=8,max_value=16,value=16)

if st.button("Generate Now"):
    pass_all = "".join(([pass_dict.get(key) for key in m_s]))
    password = "".join(random.sample(pass_all, length))
    st.code(password)