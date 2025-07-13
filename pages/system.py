import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Encriptador", page_icon=":material/encrypted_add:", layout="wide", initial_sidebar_state="collapsed")

#centered
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

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ROOT SYSTEM</title>
  <style>
    :root {
      --green: #66ff66;
    }

    * {
      box-sizing: border-box;
    }

    body {
      background-color: #000;
      background: radial-gradient(#177317, #000);
      box-shadow: inset 0 0 30rem #000000;
      color: #66ff66;
      padding: 1rem;
      margin: 0;
      font-size: 1.5rem;
      text-shadow: 0 0 5px rgb(102, 255, 102);
      font-family: "VT323", monospace;
      height: 100vh;
      overflow: hidden;
    }

    #terminal-history {
      margin: 0;
      padding: 0;
      list-style: none;
    }

    #caret {
      position: relative;
      display: inline-block;
      background-color: var(--green);
      width: 8px;
      height: 1.5rem;
    }

    #caret.blinking {
      animation: blink 1s steps(5, start) infinite;
      -webkit-animation: blink 1s steps(5, start) infinite;
    }

    
    @keyframes blink {
      to {
        visibility: hidden;
      }
    }

    @-webkit-keyframes blink {
      to {
        visibility: hidden;
      }
    }

    #alert {
      position: fixed;
      left: 50%;
      top: 50%;
      transform: translate3d(-50%, -50%, 0);
      font-size: 2.5em;
      pointer-events: none;
      animation: blink 1s steps(5, start) infinite;
    }

    #alert.hidden {
      display: none;
    }
    
        /*se agrega codigo de boton de reinicio */
    #restart-btn {
      position: fixed;
      bottom: 20px;
      right: 30px;
      background-color: black;
      color: var(--green);
      border: 2px solid var(--green);
      padding: 10px 20px;
      font-family: "VT323", monospace;
      font-size: 1.2rem;
      cursor: pointer;
      display: none;
    }

    #access-msg {
      position: fixed;
      bottom: 100px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 2em;
      display: none;
    }
    /*---------------------------------------*/
    
    
  </style>
</head>
<body>
  <ul id="terminal-history"></ul>
  <div id="terminal-input">
    <span id="terminal-text"></span><span id="caret" class="blinking"></span>
  </div>
  <div id="alert" class="hidden">SYSTEM UNDER ATTACK ABORT...</div>
  <button id="restart-btn" onclick="location.reload()">Reiniciar root system</button>
  <div id="access-msg">Access to Encryptor...</div>

  <script type="module">
    console.clear();

    String.prototype.replaceAt = function(index, replacement) {
        return this.substring(0, index) + replacement + this.substring(index + replacement.length);
    }

    const historyEl = document.querySelector('ul#terminal-history');
    const terminalText = document.querySelector('#terminal-text');
    const delay = 200;
    let currentText = "";

    const katakana = 'アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズブヅプエェケセテネヘメレヱゲゼデベペオォコソトノホモヨョロヲゴゾドボポヴッン';
    const latin = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const nums = '0123456789';

    const characters = `${latin}${nums}`;

    const initialMsgs = [           
      "Initializing hardware... [OK]",
      "Loading system files... [OK]",
      "Starting network services... [OK]",
      "System ready.",
      "Enter passwords or commands",
      "to access the encryptor...",
      "<b>to hack write: system</b>"
    ];

    init();

    function init() {
      delayMsg("*** Welcome to the root system to access the scripter***", delay / 2);
      setTimeout(displayMsgs, delay);
    }

    function displayMsgs() {
      setTimeout(() => {
        for (let i = 0; i < initialMsgs.length; i++) {
          const randomInterval = Math.random() * 1000 + (i === initialMsgs.length - 1 ? (delay * i) * 3 : delay * i);
          delayMsg(initialMsgs[i], i * randomInterval);
        }
      }, delay);
    }

    function delayMsg(msg, ms) {
      setTimeout(() => {
        historyEl.insertAdjacentHTML("beforeend", `<li>${msg}</li>`);
      }, ms);
    }

    function updateTerminalText() {
      terminalText.textContent = currentText;
    }
    
    /* --------- modificacion de input Terminal text -----------*/
    /*
    function inputTerminalText() {
      if (currentText.toLowerCase() === "system") {
        glitchOut();
      } else {
        historyEl.insertAdjacentHTML("beforeend", `<li>${currentText}</li>`);
      }
    }
    */
        
    function inputTerminalText() {
      const input = currentText.toLowerCase();

      if (input === "system") {
        glitchOut();
      } else if (input === "bootencryptor") {
        historyEl.insertAdjacentHTML("beforeend", `<li>${currentText}</li>`);
        accessEncryptor();
      } else {
        historyEl.insertAdjacentHTML("beforeend", `<li>${currentText}</li>`);
      }
    }


    function glitchOut() {
      document.querySelector('#caret').classList.remove('blinking');
      document.querySelectorAll('ul#terminal-history > li').forEach((li, i) => {
        const text = li.textContent;
        const textLength = text.length;
        setTimeout(() => {
          let iLetter = 0;
          const interval = setInterval(() => {
            const randomChar = Math.floor(Math.random() * characters.length);
            let characterSet = Math.random() < 0.9 ? characters : katakana;
            let newChar = Math.random() > 0.3 ? characterSet[randomChar] : ' ';
            newChar = Math.random() < 0.9 ? newChar : newChar + characterSet[Math.floor(Math.random() * characterSet.length)];
            let newStr = li.textContent.replace(text[iLetter], newChar);
            li.textContent = newStr;
            iLetter++;
            if (iLetter >= text.length) {
              if (i === 0) {
                displayAlert();
              }
              clearInterval(interval);
            }
          }, 100);
        }, 1000);
      });
    }

    function displayAlert() {
      document.querySelector('#alert').classList.remove('hidden');
      /*se agrega el mostrar el boton */
      document.querySelector('#restart-btn').style.display = 'block';
    }
    /*se agrega funcion de acceso al encryptador */
    function accessEncryptor() {
      const msgBox = document.getElementById("access-msg");
      msgBox.style.display = "block";
      setTimeout(() => {
        window.location.href = "/encrypto";
      }, 3000);
    }
    
    
    /*
    window.addEventListener('keyup', e => {
      const key = e.key;
      if (key.toLowerCase() === "enter") {
        inputTerminalText();
        currentText = currentText.toLowerCase() === 'system' ? '' : '';
      } else if (key.toLowerCase() === "backspace") {
        currentText = currentText.length ? currentText.slice(0, -1) : currentText;
      } else if (`${latin + " "}`.toLowerCase().includes(key.toLowerCase())) {
        if (currentText.toLowerCase() === "system") {
          return false;
        } else {
          currentText += key;
        }
      }
      updateTerminalText();
    });
    */
    
    /*modificacion de ingreso de texto*/
    window.addEventListener('keyup', e => {
      const key = e.key;
      if (key.toLowerCase() === "enter") {
        inputTerminalText();
        currentText = '';
      } else if (key.toLowerCase() === "backspace") {
        currentText = currentText.length ? currentText.slice(0, -1) : currentText;
      } else if (`${latin + " "}`.toLowerCase().includes(key.toLowerCase())) {
        currentText += key;
      }
      updateTerminalText();
    });   
    
  </script>
</body>
</html>
"""

components.html(html_code, height=700 , scrolling=True)
