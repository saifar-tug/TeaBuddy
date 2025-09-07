import streamlit as st
import requests
import json
import random
from datetime import datetime

st.set_page_config(page_title="TeaBuddy - Matcha Assistant", page_icon="🍵", layout="centered")

#for context
system_prompt = """You are TeaBuddy – a friendly, helpful expert on tea, especially matcha.
Answer any healthy drinks or tea-related question helpfully, including comparisons, time of day suggestions,
and alternative healthy drinks. If someone mentions ‘Green Tea’, assume they might mean non-matcha too.
"""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#emoji reactions
short_responses = [
    "🍃 TeaBuddy liked it brief but sweet!",
    "🫖 A small sip of matcha wisdom!",
    "💚 Just the right amount of tea!"
]
long_responses = [
    "📚🍵 That was quite the tea thesis!",
    "🧠 So much steeped in that answer!",
    "🌿 Matcha deep dive alert!",
    "🫖 That was steeped to perfection!",
    "🧃 Full of flavorful tea facts!"
]

st.markdown("# 🍵 TeaBuddy - Your Matcha Assistant")
st.markdown("Hey Saif! Ask me anything about Tea or any healthy drinks, specially Matcha!!!")

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your question:", placeholder="After typing press Enter or click to Ask...")   
    model_name = st.selectbox("Choose Ollama model (v1):", ["gemma3:1b"], index=0)
    submitted = st.form_submit_button("Ask")

if submitted and user_input:
    full_prompt = f"{system_prompt}\nUser: {user_input}\nAssistant:"
    try:
        with st.spinner("Brewing your answer... 🍃"):
            res = requests.post(
                "http://localhost:11434/api/generate",
                data=json.dumps({
                    "model": model_name,
                    "prompt": full_prompt,
                    "stream": False
                })
            )
            res.raise_for_status()
            output = res.json()["response"]
            st.session_state.chat_history.append((user_input, output))
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

if st.session_state.chat_history:
    st.divider()
    for q, a in reversed(st.session_state.chat_history):
        st.markdown(f"**Saif:** {q}")
        if len(a) > 300:
            st.success(random.choice(long_responses))
        else:
            st.success(random.choice(short_responses))
        st.write(a)

if st.session_state.chat_history:
    if st.button("Save chat to file"):
        filename = f"teabuddy_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for q, a in st.session_state.chat_history:
                f.write(f"Saif: {q}\nTeaBuddy: {a}\n\n")
        st.success(f"Chat saved as `{filename}`")
