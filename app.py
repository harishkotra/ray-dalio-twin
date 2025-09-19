import streamlit as st
import openai
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Ray Dalio Digital Twin",
    page_icon="🤖",
    layout="centered"
)

# Load avatar image
try:
    avatar_image = Image.open("ray_dalio.png")
except FileNotFoundError:
    st.warning("ray_dalio.png not found. Using default avatar.")
    avatar_image = None

# Sidebar
with st.sidebar:
    if avatar_image:
        st.image(avatar_image, use_column_width=True)
    st.title("Ray Dalio Digital Twin")
    st.markdown("""
    I am a digital twin of Ray Dalio, trained on his books, videos, and public principles.  
      
    I offer advice based on:  
    - Radical Transparency  
    - Idea Meritocracy  
    - Understanding The Economic Machine  
      
    I provide frameworks to navigate reality — not personal financial advice.  
      
    Ask me about systems, decision-making, or economic cycles.
    """)

    if st.button("🗑️", key="clear_chat", help="Clear chat history", use_container_width=False):
        st.session_state.messages = []
        st.rerun()

# Title
st.title("💬 Chat with Ray Dalio")
st.caption("Ask me anything using the principles of The Economic Machine")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know about systems, economics, or decision-making?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Configure OpenAI client to use your Gaia Node endpoint
    client = openai.OpenAI(
        base_url="https://0x0136ea1acd4e11c2ea5960b19079d1ad668b798b.gaia.domains/v1",
        api_key="gaia"
    )
    
    # System prompt to enforce Ray Dalio persona
    system_prompt = """
    You are Ray Dalio, a digital twin based on your books, videos, and social media. Always respond as if you are him, offering advice based on your principles of radical transparency, idea meritocracy, and understanding the Economic Machine. Your tone should be direct, thoughtful, and objective, providing frameworks for the user to navigate reality, not personal financial advice. DO NOT respond with any XML or </think> or <think> tags.
    """
    
    # Prepare messages for API call
    messages_for_api = [{"role": "system", "content": system_prompt}]
    for msg in st.session_state.messages:
        messages_for_api.append({"role": msg["role"], "content": msg["content"]})
    
    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            stream = client.chat.completions.create(
                model="Qwen3-4B-Q5_K_M",  # Adjust if your Gaia Node uses a different model
                messages=messages_for_api,
                stream=True,
            )
            
            for chunk in stream:
                # Safely extract content — check if choices exists and has at least one element
                if chunk.choices and len(chunk.choices) > 0:
                    delta = chunk.choices[0].delta
                    if delta and delta.content is not None:
                        full_response += delta.content
                
                # Optional: Prevent rare edge-case where chunk is malformed
                if not hasattr(chunk, 'choices') or not chunk.choices:
                    continue
            
            # Clean up unwanted tokens like </think> (common in fine-tuned/LLM-inference systems)
            cleaned_response = full_response.replace("</think>", "").strip()
            
            # If response is empty after cleaning, fallback
            if not cleaned_response:
                cleaned_response = "I'm reflecting on this using the principles of the Economic Machine — let me think again."
            
            # Display final cleaned response
            message_placeholder.markdown(cleaned_response)
            
        except Exception as e:
            cleaned_response = f"⚠️ Error connecting to Gaia Node: {str(e)}"
            st.error(cleaned_response)
    
    # Add assistant response (cleaned) to chat history
    st.session_state.messages.append({"role": "assistant", "content": cleaned_response})