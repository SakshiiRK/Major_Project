import streamlit as st
from Major_Project.UI.database import login_user

def show_login(navigate):

    st.markdown(
        """
        <style>

        /* 🌌 GALAXY BACKGROUND (same as landing) */
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.95)),
                        url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=1600&q=80');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        /* CENTER CONTAINER */
        .main-container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding-top: 80px;
        }

        /* 💎 GLASS CARD */
    
        /* ✨ TITLE */
        .login-card h1 {
            color: #ffffff !important;
            font-weight: 800 !important;
            font-size: 2.2rem !important;
            text-align: center;
            margin-bottom: 10px;
        }

        .login-card p {
            color: #94a3b8 !important;
            text-align: center;
            margin-bottom: 30px;
        }

        /* INPUT */
        .stTextInput input {
            background-color: rgba(255, 255, 255, 0.08) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            color: white !important;
            border-radius: 12px !important;
            padding: 12px !important;
        }

        .stTextInput label {
            color: #cbd5e1 !important;
        }

        /* 🚀 PRIMARY BUTTON (same as landing theme) */
        div.stButton > button:first-child {
            background: linear-gradient(135deg, #0a141a, #162d3a, #1f3f52);
            color: white !important;
            border-radius: 12px !important;
            height: 3.2rem;
            font-weight: 600 !important;
            border: none !important;
            transition: all 0.3s ease;
        }

        div.stButton > button:first-child:hover {
            transform: scale(1.04);
            background: linear-gradient(135deg, #162d3a, #1f3f52, #0a141a);
        }

        /* 🔗 SECONDARY BUTTON */
        div.stButton > button[key="signup_btn"] {
            background: transparent !important;
            border: 1px solid rgba(255,255,255,0.2) !important;
            color: #cbd5e1 !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # CENTER ALIGN
    _, col, _ = st.columns([1, 2, 1])

    with col:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        if "signup_success" in st.session_state:
            st.success(st.session_state.signup_success)
            del st.session_state.signup_success
        st.markdown("<h1>Welcome Back</h1>", unsafe_allow_html=True)
        st.markdown("<p>Sign in to continue your journey </p>", unsafe_allow_html=True)

        username = st.text_input("Email", placeholder="admin@galaxy.com")
        password = st.text_input("Password", type="password")

        st.write("")

        if st.button(" Sign In", use_container_width=True):
            user = login_user(username, password)

            if user:
                st.session_state.logged_in = True
                navigate("dashboard")
            else:
                st.error("Invalid credentials")

        st.markdown("<div style='text-align:center; margin:15px 0; color:#64748b;'>or</div>", unsafe_allow_html=True)

        if st.button("Create Account", key="signup_btn", use_container_width=True):
            navigate("signup")

        st.markdown('</div>', unsafe_allow_html=True)
