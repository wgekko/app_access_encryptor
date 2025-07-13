import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Encryptor", page_icon=":material/encrypted_add:", layout="wide", initial_sidebar_state="collapsed")
# propiedad de layout centered

# Ocultar menú de tres puntos y botón Deploy
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display: none;}
    </style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Carga archivos estáticos
with open("./components/styles.css") as f:
    css_content = f.read()
with open("./components/scripts.js") as f:
    js_content = f.read()

html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Encryptor</title>
    <style>{css_content}</style>
</head>
<body>
    <div class="app-container">
        <header class="app-header">
            <div class="app-title">
                <h1>Text Encryptor</h1>
                <div class="title-glow"></div>
            </div>
            <div class="key-container">
                <label for="encryption-key">Encryption Key</label>
                <div class="input-wrapper">
                    <input type="text" id="encryption-key" value="codice" placeholder="Enter encryption key">
                    <div class="input-glow"></div>
                </div>
                <button class="help-button" id="show-instructions">?</button>
            </div>
        </header>

        <div class="instructions-panel" id="instructions-panel">
            <h2>How to use Glitch Crypt</h2>
            <ol>
                <li>Set your encryption key</li>
                <li>Enter notes in the input</li>
                <li>Click "Encrypt" to convert your text</li>
                <li>Share the encrypted text and key with your recipient</li>
                <li>Paste the encrypted text and enter the correct encryption key</li>
                <li>Click "Decrypt" to reveal the original message</li>
            </ol>
            <button class="dismiss-button" id="dismiss-instructions">Dismiss</button>
        </div>

        <div class="content-area">
            <div class="text-container">
                <div class="text-area-wrapper">
                    <label for="input-text">Input Text</label>
                    <textarea id="input-text" placeholder="Enter text to encrypt or decrypt..."></textarea>
                    <div class="textarea-glow"></div>
                </div>

                <div class="control-buttons">
                    <button id="encrypt-btn" class="action-button encrypt">
                        <span class="button-text">Encrypt</span>
                        <div class="button-glow"></div>
                    </button>
                    <button id="decrypt-btn" class="action-button decrypt">
                        <span class="button-text">Decrypt</span>
                        <div class="button-glow"></div>
                    </button>
                </div>

                <div class="text-area-wrapper">
                    <label for="output-text">Output Text</label>
                    <textarea id="output-text" readonly placeholder="Output will appear here..."></textarea>
                    <div class="textarea-glow"></div>
                </div>
            </div>
        </div>

        <footer class="app-footer">
            <div class="footer-elements">
                <div class="status-indicator">
                    <span class="status-dot"></span>
                    <span class="status-text">Secure Connection</span>
                </div>
                <div class="created-by">
                    <!-- <span>Secure Encryption</span> -->
                    <button class="home-button" onclick="window.location.href='/'">Secure Encryption</button>                    
                </div>
            </div>
        </footer>
    </div>
  <script>{js_content}</script>
</body>
</html>
"""

html(html_code, height=900)
