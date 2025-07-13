# 🟢 BootEncryptor: Encriptador Retro al Estilo Ochentoso
los codigos base o fuentes son obtenidos de https://codepen.io/
1. 
https://codepen.io/AshlynD/pen/pvodwNe
2.
https://codepen.io/Colt4D5/pen/LEYmgxK
3.
https://codepen.io/AshlynD/pen/ZYEryje

App_access_encryptor es una aplicación web con un diseño inspirado en la estética de los sistemas de los años 80. Combina una interfaz visual retro con funcionalidades modernas de encriptación de texto.

## 🧰 Funcionalidades Principales

1. **Pantalla Inicial: Teclado + Contador de Intentos**
   - Se presenta un teclado en pantalla.
   - Un contador muestra los intentos restantes para ingresar la palabra clave correcta.

2. **Pantalla de Autenticación Retro**
   - Interfaz con fondo verde y diseño tipo terminal de los 80s.
   - El usuario debe ingresar la **palabra clave correcta** para continuar.
   - Palabras clave posibles:
     - `bootencryptor`: acceso concedido al encriptador.
     - `system`: acceso denegado y el sistema se **bloquea**.
   - Si el sistema se bloquea, se muestra un **botón de reinicio** para reiniciar la aplicación.

3. **Pantalla de Encriptación de Texto**
   - Si se accede correctamente, se muestra una herramienta para **encriptar texto**.
   - Interfaz simple, efectiva y manteniendo el estilo ochentoso.

## 🔐 Palabra Clave

| Palabra | Acción                                  |
|---------|-----------------------------------------|
| bootencryptor | Accede al encriptador.               |
| system     | Bloquea el sistema.                  |

## 🔁 Reinicio del Sistema

En caso de bloqueo, el usuario puede **reiniciar** el sistema para volver a intentar ingresar la palabra clave.

## 💾 Tecnologías Usadas

- HTML/CSS (estética retro terminal)
- JavaScript (lógica de navegación y encriptación)
- Python-Streamlit (framework)
- [Opcional: framework que uses, como React o Vue]

para correr la app debe hacerse desde la terminal  y escribir streamlit run app.py

video demo 



https://github.com/user-attachments/assets/f81948f7-2095-4752-a14f-2272ea637248



## 🚀 Cómo Ejecutar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/wgekko/app_access_encryptor
   cd app_access_encryptor
