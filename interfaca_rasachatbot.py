import streamlit as st
import requests

st.set_page_config(page_title="Chatbot Rasa", page_icon="🤖")

st.title("💬 Interface Chatbot Rasa (arabe)")
st.markdown("Testez votre assistant directement ici.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Champ de saisie utilisateur
user_input = st.text_input("Vous :", "", key="user_input")

# Envoie de la requête à Rasa lorsque l'utilisateur saisit un message
if user_input:
    st.session_state.chat_history.append(("🧑", user_input))

    try:
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            json={"sender": "user", "message": user_input}
        )
        bot_responses = response.json()
        if not bot_responses:
            st.session_state.chat_history.append(("🤖", "Désolé, je n'ai pas compris."))
        for r in bot_responses:
            st.session_state.chat_history.append(("🤖", r.get("text", "…")))
    except requests.exceptions.ConnectionError:
        st.error("❌ Le serveur Rasa ne répond pas. L'avez-vous lancé avec `rasa run` ?")

# Affichage de l'historique de la conversation
for speaker, message in st.session_state.chat_history:
    if speaker == "🧑":
        st.markdown(f"**Vous :** {message}")
    else:
        st.markdown(f"**Bot :** {message}")
