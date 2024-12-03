from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from google.cloud import aiplatform
from google.oauth2 import service_account
import vertexai
from vertexai.preview.generative_models import GenerativeModel
import config  # ייבוא קובץ הקונפיגורציה

# טעינת האישורים מתוך הקובץ config
credentials = service_account.Credentials.from_service_account_file(config.credentials_path)

# אתחול Vertex AI עם האישורים
aiplatform.init(
    project=config.project_id,
    location=config.location,
    credentials=credentials
)

vertexai.init(
    project=config.project_id,
    location=config.location,
    credentials=credentials
)

# הגדרת המודל הגנרטיבי
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
model = GenerativeModel("gemini-pro", generation_config=generation_config)

# פקודת /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = """Hello there! I'm Gemini 🤖, your friendly chatbot. I can answer your questions in a conversational manner and even recognize the contents of images. Let's get started!

/chat - Initiate a chat with me.
/image - Share an image and learn about its contents.

This bot was created by Yaniv Logi. Check out my portfolio here: [Yaniv Logi's Portfolio](https://yanivlogi.github.io/portfolio/)

Feel free to explore and ask me anything!"""
    await update.message.reply_text(text, parse_mode="Markdown")

# פקודת /chat
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text.replace("/chat", "").strip()
    if not user_input:
        await update.message.reply_text("Send me a message after the /chat command, and I'll reply!")
        return

    response = model.start_chat(history=[]).send_message(user_input).text
    await update.message.reply_text(response)

# פקודת fallback
async def fallback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("I didn't recognize that command. Try /start, /chat, or /image.")

# הפעלת הבוט
if __name__ == "__main__":
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("chat", chat))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fallback))
    print("Bot is running...")
    app.run_polling()
