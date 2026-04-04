import streamlit as st

def show_welcome(navigate):

    # --- PAGE CONFIG ---
    st.set_page_config(page_title="Lesson Planning", layout="wide")

    # --- CUSTOM CSS ---
    st.markdown(
        """
        <style>

        /* BACKGROUND */
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.95)), 
                        url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=1600&q=80');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        /* HERO TEXT */
        .hero-text-container {
            padding: 120px 0;
            color: white;
        }

        .hero-title {
            font-size: 4rem;
            font-weight: 700;
            line-height: 1.1;
        }

        .hero-subtitle {
            font-size: 1.2rem;
            opacity: 0.85;
            margin-top: 15px;
        }


        /* BUTTON STYLE */
        div.stButton > button {
            background: linear-gradient(135deg, #0a141a, #162d3a, #1f3f52);
            color: white;
            border-radius: 12px;
            height: 55px;
            font-size: 16px;
            border: none;
            font-weight: 600;
            box-shadow: 0 0 8px rgba(0, 0, 0, 0.6);
            transition: all 0.3s ease;
        }

        div.stButton > button:hover {
            background: linear-gradient(135deg, #162d3a, #1f3f52, #0a141a);
            transform: scale(1.04);
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- LAYOUT ---
    left, right = st.columns([1.5, 1], gap="large")

    # --- LEFT SIDE ---
    with left:
        st.markdown('<div class="hero-text-container">', unsafe_allow_html=True)

        st.markdown(
            '<div class="hero-title">Explore our <br>Universe.</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="hero-subtitle">Building  smarter systems.</div>',
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

    # --- RIGHT SIDE ---
    with right:
        st.write("##")

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

        st.subheader(" Get Started")
        st.write("Sign in or create an account to continue")

        st.write("")

        if st.button(" Sign In", use_container_width=True):
            navigate("login")

        st.write("")

        if st.button(" Create Account", use_container_width=True):
            navigate("signup")

        st.markdown('</div>', unsafe_allow_html=True)

