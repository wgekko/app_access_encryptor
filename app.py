#from curses import window
import streamlit as st
from streamlit.components.v1 import html
from streamlit_js_eval import streamlit_js_eval
import time
import streamlit.components.v1 as components


st.set_page_config(page_title="Codigo", page_icon=":material/encrypted_add:", layout="wide", initial_sidebar_state="collapsed")

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
# Asegúrate de que las rutas 'asset/style.css' y 'asset/script.js' sean correctas
try:
    with open("asset/style.css") as f:
        css_content = f.read()
    with open("asset/script.js") as f:
        js_content = f.read()
except FileNotFoundError:
    st.error("Error: Asegúrate de que los archivos style.css y script.js estén en la carpeta 'asset'.")
    st.stop() # Detiene la ejecución si los archivos no se encuentran

js_script = """
    document.addEventListener("DOMContentLoaded", () => {
        window.addEventListener("message", (event) => {
            if (event.data && event.data.type === "PIN_SUCCESS") {
                localStorage.setItem("PIN_SUCCESS", "true");
            }
        });
    });
"""


html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Secure Access Terminal</title>
    <style>{css_content}</style>
</head>
<body>
    <div class="container">
        <header>
            <h1 class="glitch-title">ERROR: ACCESS DENIED</h1>
        </header>
        <main>
            <section class="keypad-section">
                <div class="keypad-container">
                    <div class="pin-display">
                        <div class="pin-dots">
                            <span class="pin-dot"></span>
                            <span class="pin-dot"></span>
                            <span class="pin-dot"></span>
                            <span class="pin-dot"></span>
                        </div>
                    </div>
                    <div class="keypad-grid">
                        <button class="key" data-key="1">1</button>
                        <button class="key" data-key="2">2</button>
                        <button class="key" data-key="3">3</button>
                        <button class="key" data-key="4">4</button>
                        <button class="key" data-key="5">5</button>
                        <button class="key" data-key="6">6</button>
                        <button class="key" data-key="7">7</button>
                        <button class="key" data-key="8">8</button>
                        <button class="key" data-key="9">9</button>
                        <button class="key key-delete" data-key="delete">DEL</button>
                        <button class="key" data-key="0">0</button>
                        <button class="key key-unlock" data-key="unlock">UNLOCK</button>
                    </div>
                </div>
            </section>
            <section class="log-section">
                <div class="log-container">
                    <div class="log-header">
                        <h2>Generar Códigos Cifrados</h2>
                        <div class="attempts-counter">
                            <span class="attempts-text">INTENTOS RESTANTES:</span>
                            <span class="attempts-number">5</span>
                        </div>
                    </div>
                    <div class="log-content" id="log-content">
                        <div class="log-placeholder">
                            <div class="scanner-line"></div>
                            <p>INTRODUCIR CÓDIGO DE ACCESO</p>
                            <p>5 INTENTOS ANTES DEL BLOQUEO DE SEGURIDAD</p>
                        </div>
                    </div>
                </div>
            </section>
        </main>
        <div class="overlay"></div>
        <div class="scanlines"></div>
        <div class="glow"></div>
    </div>
<script>{js_content}</script>
<script>{js_script}</script>
</body>
</html>
"""
html(html_code, height=900)

# Agrega listener para postMessage y envía señal a Streamlit
components.html("""
<script>
 window.addEventListener("message", event => {
   if (event.data && event.data.type === "PIN_SUCCESS") {
     fetch("/", {method:"POST", body:JSON.stringify({pin:"success"})})
   }
 });
</script>
""", height=0)

# Listener para mensaje JS -> Python
html("""
<script>
window.addEventListener("message", (event) => {
    if (event.data && event.data.type === "PIN_SUCCESS") {
        const streamlitChannel = window.parent;
        streamlitChannel.postMessage({ isStreamlitMessage: true, type: "streamlit:setComponentValue", value: true }, "*");
    }
});
</script>
""", height=0)

if "pin_autorizado" not in st.session_state:
    st.session_state.pin_autorizado = False

# Captura el valor desde JS
pin_autorizado = streamlit_js_eval(js_expressions=[], key="pin_listen", default=None)

if pin_autorizado is True and not st.session_state.pin_autorizado:
    st.session_state.pin_autorizado = True
    st.success("🔓 PIN correcto. Redirigiendo...")
    st.switch_page("pages/system.py")


#if "pin_autorizado" not in st.session_state:
#    st.session_state.pin_autorizado = False    
    

# Solo revisar si aún no fue autorizado

# if not st.session_state.pin_autorizado:
#    pin_success = streamlit_js_eval(
#        js_expressions=["localStorage.getItem('PIN_SUCCESS')"],
#        key="poll_pin"
#    )
    
#    st.write("Resultado de PIN_SUCCESS:", pin_success)
    
    
#    if pin_success == "true":
#        st.session_state.pin_autorizado = True
#        st.switch_page("pages/system.py")
        #st.rerun()

#else:
#    st.success("🔓 PIN correcto detectado. Acceso concedido.")
#    if st.button("Ir al root del sistema"):
#        st.switch_page("pages/system.py")