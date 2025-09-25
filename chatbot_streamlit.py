import streamlit as st
import pandas as pd
from difflib import get_close_matches

# Load dataset
df = pd.read_csv("dreamweaver_ai_100.csv")

# Function to get a response
def get_response(user_input):
    user_input = user_input.lower()

    # Try exact or partial keyword match
    for _, row in df.iterrows():
        if user_input in row['description'].lower() or user_input in row['name'].lower():
            return f"✨ {row['name']} ({row['category']})\n{row['description']}\n🔗 Website: {row['website']}"

    # If not found, try fuzzy matching
    descriptions = df['description'].str.lower().tolist()
    matches = get_close_matches(user_input, descriptions, n=1, cutoff=0.3)

    if matches:
        matched_row = df[df['description'].str.lower() == matches[0]].iloc[0]
        return f"✨ {matched_row['name']} ({matched_row['category']})\n{matched_row['description']}\n🔗 Website: {matched_row['website']}"

    return "😴 Sorry, I couldn’t find a matching DreamWeaver AI tool."

# Streamlit UI
st.set_page_config(page_title="DreamWeaver AI Chatbot", page_icon="🌙")

st.title("🌙 DreamWeaver AI Chatbot")
st.write("Ask me about DreamWeaver AI tools and I’ll find the best match from the dataset!")

# Session state to keep chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", "")

if st.button("Send") and user_input.strip() != "":
    response = get_response(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# Display chat history
for role, msg in st.session_state.history:
    if role == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")
