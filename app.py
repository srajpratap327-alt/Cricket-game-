import streamlit as st
import random

st.title("🏏 Cricket Championship App")

if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.game_over = False

st.write(f"Aapka Score: {st.session_state.score}")

# Ek placeholder banate hain jahan result dikhega
result_placeholder = st.empty()

user_run = st.number_input("Runs chuniye (1-6):", min_value=1, max_value=6, step=1)

if st.button("Bowl Daliye!"):
    if not st.session_state.game_over:
        comp_run = random.randint(1, 6)
        
        if user_run == comp_run:
            result_placeholder.error(f"Computer ne dala: {comp_run}. OUT! Aap out ho gaye!")
            st.session_state.game_over = True
        else:
            st.session_state.score += user_run
            result_placeholder.success(f"Computer ne dala: {comp_run}. Aapka total score: {st.session_state.score}")
    else:
        result_placeholder.warning("Game khatam ho chuka hai! Naya game shuru karein.")

if st.button("Naya Game Shuru Karein"):
    st.session_state.score = 0
    st.session_state.game_over = False
    st.rerun()
    
