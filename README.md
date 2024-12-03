
# Gemini Telegram Bot

## How to Set Up

1. **Clone the repository:**
   ```bash
   git clone https://github.com/USERNAME/gemini-telegram-bot.git
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `config.py` file:**
   - Copy `config_template.py` to `config.py`.
   - Update the following fields with your own information:
     - `BOT_TOKEN`: Your Telegram Bot token (get it from @BotFather).
     - `project_id`: Your Google Cloud project ID.
     - `location`: Your Google Cloud location.
     - `credentials_path`: Path to your `credentials.json` file (download it from Google Cloud Console).
   
   Example:
   ```python
   # config.py

   # Telegram Bot Token
   BOT_TOKEN = "your_bot_token_here"

   # Google Cloud project configuration
   project_id = "your_project_id_here"
   location = "your_location_here"

   # Path to the credentials JSON file
   credentials_path = "path_to_your_credentials_file.json"
   ```

4. **Run the bot:**
   ```bash
   python Gemini-Bot.py
   ```

## Author
Created by **Yaniv Logi**  
Check out my [portfolio](https://yanivlogi.github.io/portfolio/).
