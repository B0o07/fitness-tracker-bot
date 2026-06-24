import os
import requests
import random
from datetime import datetime
# Importamos load_dotenv para ler o arquivo oculto .env
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

class DynamicFitnessBot:
    def __init__(self):
        # O script busca as credenciais de forma segura nas variáveis de ambiente
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        
        if not token or not chat_id:
            raise ValueError("[ERROR] Missing environment variables. Please check your .env file.")
            
        self.api_url = f"https://api.telegram.org/bot{token}/sendMessage"
        self.chat_id = chat_id

    def send_workout_reminder(self):
        workouts = [
            "• 5km Run (Moderate Pace)\n• 3 Sets of Core Exercises (To Failure)",
            "• 40-Minute Calisthenics Circuit\n• 4 Sets of Pull-ups & Push-ups",
            "• High-Intensity Interval Training (HIIT)\n• 20-Minute Full Body Stretch"
        ]
        
        motivations = [
            "Consistency is what transforms average effort into excellent results. Stay disciplined today!",
            "Discipline over motivation. Go get your targets done today!",
            "Every single workout counts towards the final objective. Push hard!"
        ]
        
        current_date = datetime.now().strftime("%B %d, %Y")
        selected_workout = random.choice(workouts)
        selected_motivation = random.choice(motivations)

        workout_escaped = selected_workout.replace("-", "\\-").replace("(", "\\(").replace(")", "\\)")
        motivation_escaped = selected_motivation.replace("!", "\\!").replace(".", "\\.").replace("-", "\\-")
        date_escaped = current_date.replace(",", "\\,")

        message = (
            "🎯 *DAILY GOAL REMINDER*\n"
            "───────────────────────\n"
             f"📅 *Date:* {date_escaped}\n"
             "⏰ *Time:* 06:00 PM\n\n"
             "🏃‍♂️ *Scheduled Activity:*\n"
             f"{workout_escaped}\n\n"
             "🔥 *Weekly Status:* 3/5 Workouts Completed\\!\\n"
             "───────────────────────\n"
             f"⚡ _Motivation: '{motivation_escaped}'_"
        )
        
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "MarkdownV2"
        }
        
        try:
            response = requests.post(self.api_url, json=payload)
            if response.status_code == 200:
                print("[SUCCESS] Dynamic automated alert sent successfully!")
            else:
                print(f"[ERROR] Failed to send message: {response.text}")
        except Exception as e:
            print(f"[CRITICAL] Connection failed: {e}")

if __name__ == "__main__":
    bot = DynamicFitnessBot()
    bot.send_workout_reminder()