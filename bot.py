import os
import logging
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 1. Cargar las variables de entorno desde el archivo .env
load_dotenv()
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# 2. Configurar el sistema de logs (para ver errores en la terminal)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 3. Comando /start: Saludo inicial
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 ¡Hola! Soy tu asistente DevOps.\n"
        "Usa /status para revisar tus servicios o /check <url> para verificar una web."
    )

# 4. Comando /status: Revisa una web fija (ejemplo: GitHub)
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://github.com"
    await update.message.reply_text(f"🔍 Verificando el estado de {url}...")
    
    try:
        # Hacemos una petición HTTP GET con un tiempo límite de 5 segundos
        response = requests.get(url, timeout=5)
        
        # Si el código de respuesta es 200 (OK), la web está arriba
        if response.status_code == 200:
            await update.message.reply_text(f"✅ {url} está OPERATIVO (Status: 200 OK).")
        else:
            await update.message.reply_text(f"⚠️ {url} reporta problemas (Status: {response.status_code}).")
            
    except requests.exceptions.RequestException:
        # Si hay un error de conexión o timeout, la web está caída
        await update.message.reply_text(f"🚨 ¡ALERTA! No se pudo conectar con {url}. El sitio podría estar caído.")

# 5. Función principal que arranca el bot
def main():
    if not TOKEN:
        print("❌ Error: No se encontró el TELEGRAM_TOKEN en las variables de entorno.")
        return

    # Crear la aplicación del bot con el token seguro
    app = Application.builder().token(TOKEN).build()

    # Registrar los comandos que el bot va a escuchar
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    # Iniciar el bot (se queda escuchando eventos hasta que lo detengas)
    print("🤖 Bot iniciado y escuchando comandos...")
    app.run_polling()

if __name__ == '__main__':
    main()