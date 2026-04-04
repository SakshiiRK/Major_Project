import streamlit as st
from Major_Project.UI.database import create_user

def show_signup(navigate):

    st.markdown(
        """
        <style>

        /* 🌌 SAME GALAXY BACKGROUND */
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.95)),
                        url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=1600&q=80');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        /* 💎 GLASS CARD */

        /* ✨ TITLE */
        .signup-card h1 {
            color: #ffffff !important;
            font-weight: 800 !important;
            font-size: 2.2rem !important;
            text-align: center;
            margin-bottom: 10px;
        }

        .signup-card p {
            color: #94a3b8 !important;
            text-align: center;
            margin-bottom: 25px;
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

        /* 🚀 PRIMARY BUTTON (match login + landing) */
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
        div.stButton > button[key="back_login_btn"] {
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
        st.markdown('<div class="signup-card">', unsafe_allow_html=True)

        st.markdown("<h1>Create Account</h1>", unsafe_allow_html=True)
        st.markdown("<p>Start your journey in the galaxy </p>", unsafe_allow_html=True)

        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        password = st.text_input("Create Password", type="password")

        st.write("")

        if st.button("Register Now", use_container_width=True):
            success = create_user(name, email, password)

            if success:
                st.session_state.signup_success = "Account created successfully"
                navigate("login")
            else:
                st.error("User already exists")

        st.markdown("<div style='text-align:center; margin:15px 0; color:#64748b;'>or</div>", unsafe_allow_html=True)

        if st.button(" Back to Login", key="back_login_btn", use_container_width=True):
            navigate("login")

        st.markdown('</div>', unsafe_allow_html=True)
        print("Hello, World!")

