import streamlit as st
import json
import groq_utils

st.set_page_config(page_title="🧠 Flashcard Generator", page_icon="📚", layout="wide")

client = groq_utils.init_groq_client()

st.title("📚 FlashForge AI")
st.markdown("Upload a **PDF of study material** and generate **AI-powered flashcards** using Groq's Llama 4 model.")

#  PDF File Uploader
uploaded_file = st.file_uploader("Please upload your **lecture notes** or **study material** (PDF format only)", type=["pdf"])

if uploaded_file is None:
    st.info("👆 Please upload a PDF to get started. Once uploaded, flashcards will be generated automatically.")
    st.stop()  # Wait for user to upload a file

with st.spinner("Extracting PDF text..."):
    full_text = groq_utils.extract_text_from_pdf(uploaded_file)

st.success("PDF processed successfully.")
chunk_size = 2000  # Break text into chunks
chunks = [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size)]

if st.button("⚡ Generate Flashcards"):
    flashcards = []
    with st.spinner("Generating flashcards with Groq..."):
        for i, chunk in enumerate(chunks):
            result = groq_utils.generate_flashcards(client, chunk)
            flashcards.append(result)

    st.subheader("🧠 Your Flashcards")
    
    card_counter = 1  # Initialise a counter to keep track of the card number
    for i, block in enumerate(flashcards):
        cards = block.strip().split("\n\n")
        for card in cards:
            if card.strip():
                # Each card contains the question and the answer
                question, answer = card.strip().split("\n", 1)
                with st.expander(f"Card {card_counter}: {question}"):
                    st.markdown(f"{answer.strip()}")
                card_counter += 1

    all_text = "\n\n".join(flashcards)
    st.download_button("⬇️ Download Flashcards", all_text, "flashcards.txt", "text/plain")

st.divider()
st.caption("🚀 Powered by Groq (LLaMA 4 Scout)")
st.caption("👨‍💻 Built by Hugo Miloszewski")
