import streamlit as st

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# 🔥 HIDE SIDEBAR COMPLETELY
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
[data-testid="stHeader"] {display: none;}
footer {display: none;}
</style>
""", unsafe_allow_html=True)

# Initialize session
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# Navigation
def navigate(page):
    st.session_state.page = page
    st.rerun()

# Routing
if st.session_state.page == "welcome":
    from Major_Project.UI.pages.welcome import show_welcome
    show_welcome(navigate)

elif st.session_state.page == "login":
    from Major_Project.UI.pages.login import show_login
    show_login(navigate)

elif st.session_state.page == "signup":
    from Major_Project.UI.pages.signup import show_signup
    show_signup(navigate)

elif st.session_state.page == "dashboard":
    from Major_Project.UI.pages.dashboard import show_dashboard
    show_dashboard(navigate)
