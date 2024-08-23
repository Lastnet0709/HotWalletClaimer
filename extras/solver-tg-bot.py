import os
import sys
import logging
import re
import requests
import base64
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Tokens
BOT_TOKEN = ''
GITHUB_TOKEN = ''

# GitHub settings
REPO = "thebrumby/HotWalletClaimer"
PATH = "extras/rewardtest"
BRANCH = "main"

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Received /start command")
    await update.message.reply_text("Bot is up and running. Use /set <code> to update GitHub.")

async def set_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        code = context.args[0]
        if re.match(r'^\d{4}$', code):
            logger.info(f"Received valid code: {code}")
            await update.message.reply_text(f"Received code: {code}. Attempting to update GitHub...")
            success = await write_code_to_github(code)
            if success:
                await update.message.reply_text(f"Code {code} successfully updated on GitHub.")
            else:
                await update.message.reply_text(f"Failed to update code {code} on GitHub.")
        else:
            await update.message.reply_text("Invalid code format. Please enter a 4-digit code.")
    else:
        await update.message.reply_text("Please provide a 4-digit code. Usage: /set <code>")

async def write_code_to_github(code):
    api_url = f"https://api.github.com/repos/{REPO}/contents/{PATH}"

    try:
        logger.info(f"Attempting to fetch current file SHA from GitHub at {api_url}")
        # Get the file's current SHA
        response = requests.get(api_url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
        response.raise_for_status()  # Will raise an exception for 4xx/5xx errors
        sha = response.json().get("sha")
        if not sha:
            logger.error("No SHA found in GitHub response")
            return False

        logger.info(f"SHA retrieved: {sha}")

        # Create the content to update (encoded in base64)
        content = code + "\n"
        encoded_content = base64.b64encode(content.encode()).decode()

        # Prepare the request data
        data = {
            "message": f"Update rewardtest with code {code}",
            "content": encoded_content,
            "sha": sha,
            "branch": BRANCH
        }

        # Send the PUT request to update the file
        logger.info("Sending PUT request to update the file on GitHub")
        response = requests.put(api_url, json=data, headers={"Authorization": f"token {GITHUB_TOKEN}"})
        response.raise_for_status()

        logger.info(f"Successfully wrote code {code} to GitHub.")
        return True

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to write code to GitHub: {e}")
        return False

def main():
    try:
        # Initialize the Application
        logger.info("Initializing the bot application")
        application = Application.builder().token(BOT_TOKEN).build()

        # Register handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("set", set_code))

        # Log the startup
        logger.info("Bot is starting...")

        # Start the bot
        application.run_polling()

    except Exception as e:
        logger.error(f"An error occurred in the main function: {e}", exc_info=True)
        sys.exit(1)  # Ensure the script exits on critical error

if __name__ == "__main__":
    main()