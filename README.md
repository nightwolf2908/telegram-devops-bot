# 🤖 Telegram Event-Driven DevOps Bot

![CI Pipeline](https://github.com/nightwolf2908/telegram-devops-bot/actions/workflows/devops-ci.yml/badge.svg)

Proyecto desarrollado en Python para el monitoreo automatizado de infraestructura y servicios web basado en eventos. Demuestra el consumo de APIs externas y la gestión segura de credenciales.

## 🚀 Características
- **Arquitectura basada en eventos:** Escucha activa de comandos a través de la API de Telegram.
- **Monitoreo de disponibilidad:** Verificación de estados HTTP (Uptime/Downtime) en tiempo real mediante requests asíncronos.
- **Seguridad (DevOps Best Practices):** Aislamiento estricto de secretos y tokens mediante variables de entorno (`.env`).
- **Pipeline de Integración Continua (CI):** Automatización de flujos de trabajo mediante GitHub Actions para validar cada cambio en el código en un entorno limpio de Ubuntu Linux.
- **Calidad de Código y Linting:** Implementación de `flake8` dentro del pipeline para realizar análisis estáticos de sintaxis, garantizando que el código cumpla con los estándares profesionales antes de ser aprobado.
- **Gestión Avanzada de Secretos (DevOps Security):** Uso de GitHub Secrets para inyectar de forma segura el token de la API en el entorno de ejecución de GitHub Actions, evitando la exposición de credenciales en el historial de Git.

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