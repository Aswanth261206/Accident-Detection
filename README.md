# Accident Alert Simulator

## Project Description
Accident Alert Simulator is a beginner-friendly Python mini project that simulates an emergency accident response system. It collects accident details, validates severity input, sends instant alerts to Telegram using a free Telegram Bot, and prints response actions based on how serious the accident is.

## Features
- Professional command-line heading with current date and time
- User input for accident location, victim name, and emergency contact number
- Severity validation using `try-except` (accepts only integers from 1 to 10)
- Function-based structure for clean and reusable code
- Severity-based response flow for serious vs minor accidents
- Sends full accident details via Telegram Bot to a demo chat (`9363765396`) - completely free
- Loop-based simulation mode to test multiple accident scenarios in one run
- Clean console formatting using separators (`=` and `-`)

## Technologies Used
- Python 3
- Built-in modules: `datetime`, `os`
- External library: `requests`
- Alerting: Telegram Bot API (free)

## How to Run the Project
1. Open a terminal in the project folder.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a Telegram Bot and get your bot token:
   - Open Telegram and search for `@BotFather`
   - Send `/start` and `/newbot`
   - Follow the steps to create a bot
   - Copy your bot token (e.g., `123456789:ABCDefGHIjklmno...`)

4. Get your Telegram Chat ID:
   - Send any message to your bot
   - Open `https://api.telegram.org/bot<your_bot_token>/getUpdates`
   - Find your `chat_id` in the response

5. Set your Telegram Bot token (Windows PowerShell):

```powershell
$env:TELEGRAM_BOT_TOKEN="8329672495:AAHNpamxpr0INod9YMxlBkDz2t4_1rDPB4c"
```

6. Run the program:

```bash
python main.py
```

If the bot token is not set, the program still runs but alerts are skipped with a setup warning.

Note: Telegram Bot is completely free - no charges, no verification needed!

## Example Output
```text
======================================================================
                 EMERGENCY ACCIDENT ALERT SYSTEM
======================================================================
Current Date & Time: 2026-04-13 10:45:17
----------------------------------------------------------------------
Enter accident location: Main Street Junction
Enter victim name: Riya Sharma
Enter emergency contact number: 9876543210
Enter accident severity (1-10): 8

----------------------------------------------------------------------
Location: Main Street Junction
Victim Name: Riya Sharma
Emergency Contact: 9876543210
Severity Level: 8/10
----------------------------------------------------------------------
SERIOUS ACCIDENT DETECTED
Sending emergency alert to nearest hospital...
Informing victim's family...
Sharing accident location with emergency services...
======================================================================
Do you want to test another accident? (yes/no): no

Thank you for using the Emergency Accident Alert System.
```

## Suggested GitHub Repository Description
A Python-based emergency accident response simulator that validates incident severity, sends Telegram alerts, and triggers safety workflows for public-safety learning projects.

## Suggested GitHub Tags
`python` `simulation` `public-safety` `emergency-response` `telegram` `telegram-bot` `alerts` `beginner-project` `cli` `mini-project`
