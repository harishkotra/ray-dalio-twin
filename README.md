# 🌊 Ray Dalio Digital Twin — Chat with the Economic Machine

> *“The most important thing is to understand reality.”*  
> — Ray Dalio

A simple Streamlit chat application that lets you converse with a digital twin of **Ray Dalio**, powered by your **Gaia Node** (an OpenAI-compatible endpoint). This AI responds in Ray’s voice — grounded in his principles of **radical transparency**, **idea meritocracy**, and **understanding The Economic Machine**.

No financial advice. Just frameworks. Always objective.

<img width="1645" height="1186" alt="image" src="https://github.com/user-attachments/assets/3b426499-dfa1-4849-a9e5-ca03ef2ce9d3" />
<img width="1637" height="1183" alt="image" src="https://github.com/user-attachments/assets/33e29867-8668-420f-88c1-bfafcc92c365" />


## ✨ Features

- 🤖 **Authentic Ray Dalio Persona**: Responses shaped by his books, interviews, and public philosophy.
- 💬 **Streamlit Chat UI**: Clean, intuitive, and responsive interface.
- 🖼️ **Custom Avatar**: Uses `ray_dalio.png` in the sidebar for instant recognition.
- 🔧 **OpenAI-Compatible Endpoint**: Connects directly to your Gaia Node (no OpenAI API key required).
- 🗑️ **Clear Chat Button**: Small, subtle trash icon in the sidebar to reset conversation history.
- 🚫 **No Internal Tokens**: Automatically strips artifacts like `</think>` from responses.
- ⚡ **Streaming Responses**: Real-time typing feel for natural interaction.

---

## 🛠️ Setup

### 1. Prerequisites
Make sure you have Python 3.8+ installed.

### 2. Install Dependencies
```bash
pip install streamlit openai pillow
```

### 3. Prepare Your Files
- Place your **Ray Dalio avatar image** as `ray_dalio.png` in the same folder as `app.py`.
- Replace the placeholder endpoint in `app.py`:
  ```python
  base_url="YOUR_GAIA_ENDPOINT",   # e.g., "http://localhost:8080/v1" or your hosted URL
  api_key="YOUR_API_KEY",         # leave as "" if no auth needed
  ```

> 💡 If your Gaia Node uses a different model name than `gpt-3.5-turbo`, update the `model=` parameter accordingly.

### 4. Run the App
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8080` to start chatting.

---

## 📌 Notes

- This app does **not** use OpenAI’s cloud API — it connects only to your local or private [Gaia Node](https://docs.gaianet.ai/getting-started/quick-start/).
- Responses are filtered to remove internal tokens (`</think>`) that may be injected by your backend.
- For best results, ensure your Gaia Node is running and accessible before launching the app.

---

## 🙏 Inspired By

Ray Dalio’s principles from:
- *Principles: Life and Work*
- *Principles for Dealing with the Changing World Order*
- *How the Economic Machine Works*

This is not an official product of Bridgewater Associates — just a thoughtful digital reflection.
