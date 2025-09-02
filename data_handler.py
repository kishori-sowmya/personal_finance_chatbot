import streamlit as st

# Import backend function (assumed to be provided separately)
# from backend import get_chatbot_response  

def get_chatbot_response(user_input):
    # Temporary mock function (for testing UI only)
    return f"Chatbot response to: {user_input}"


# Streamlit UI
st.set_page_config(page_title="Chatbot UI", page_icon="🤖", layout="centered")

st.title("💬 Simple Chatbot")
st.write("Type your question below and click *Send* to chat with the bot.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input box
user_input = st.text_input("You:", value="", key="input_text")

# Send button
if st.button("Send") and user_input.strip():
    # Get response from backend
    bot_response = get_chatbot_response(user_input)

    # Save to history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

    # Clear input field after sending
    st.session_state.input_text = ""

# Display chat history
st.subheader("Chat History")
for role, message in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"🧑 {role}:** {message}")
    else:
        st.markdown(f"🤖 {role}:** {message}")
