# 🤖 Telegram Event-Driven DevOps Bot

Proyecto desarrollado en Python para el monitoreo automatizado de infraestructura y servicios web basado en eventos. Demuestra el consumo de APIs externas y la gestión segura de credenciales.

## 🚀 Características
- **Arquitectura basada en eventos:** Escucha activa de comandos a través de la API de Telegram.
- **Monitoreo de disponibilidad:** Verificación de estados HTTP (Uptime/Downtime) en tiempo real mediante requests asíncronos.
- **Seguridad (DevOps Best Practices):** Aislamiento estricto de secretos y tokens mediante variables de entorno (`.env`).

## 🛠️ Tecnologías utilizadas
- **Python 3.x**
- **Librerías:** `python-telegram-bot`, `requests`, `python-dotenv`

## ⚙️ Instalación y Configuración Local

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/telegram-devops-bot.git](https://github.com/TU_USUARIO/telegram-devops-bot.git)

2. Instalar dependencias:
   pip install -r requirements.txt

3. Configurar variables de entorno: Crear un archivo .env en la raíz con tu token:
   TELEGRAM_TOKEN=tu_token_aqui

4. Ejecutar el bot:
   python bot.py