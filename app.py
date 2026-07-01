import streamlit as st
import random

st.title("🏏 Cricket Championship App")

if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.computer_score = 0
    st.session_state.game_over = False

st.write("Batting shuru karein!")

user_run = st.number_input("Runs chuniye (1-6):", min_value=1, max_value=6, step=1)

if st.button("Bowl Daliye!"):
    if not st.session_state.game_over:
        comp_run = random.randint(1, 6)
        st.write(f"Computer ne dala: {comp_run}")
        
        if user_run == comp_run:
            st.error("OUT! Aap out ho gaye!")
            st.session_state.game_over = True
        else:
            st.session_state.score += user_run
            st.success(f"Score: {st.session_state.score}")
    else:
        st.warning("Game khatam ho chuka hai! Restart karein.")

if st.button("Restart Game"):
    st.session_state.score = 0
    st.session_state.game_over = False
    st.rerun()
