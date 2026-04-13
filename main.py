"""Accident Alert Simulator: Emergency accident response workflow simulation."""

import datetime
import os

import requests

# Telegram Bot API endpoint and demo chat ID for sending accident alerts.
TELEGRAM_API_URL = "https://api.telegram.org/bot"
DEMO_CHAT_ID = "9363765396"


def display_header():
    """Display the system heading and current date/time."""
    # Print a top separator for clean and professional output formatting.
    print("=" * 70)
    # Print the main system title so users know what program is running.
    print("                 EMERGENCY ACCIDENT ALERT SYSTEM")
    # Print a bottom separator line under the title.
    print("=" * 70)
    # Capture the current local date and time using the datetime module.
    current_time = datetime.datetime.now()
    # Show the current timestamp in a readable format for report context.
    print("Current Date & Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    # Add a visual separator before user inputs start.
    print("-" * 70)


def get_severity():
    """Ask for accident severity and validate that it is an integer from 1 to 10."""
    while True:
        try:
            # Ask the user for a severity score between 1 and 10.
            severity = int(input("Enter accident severity (1-10): ").strip())
            # Check if the provided value is within the accepted range.
            if 1 <= severity <= 10:
                # Return the valid severity value to the caller.
                return severity
            # Show an error when the number is outside the valid range.
            print("Error: Severity must be between 1 and 10.")
        except ValueError:
            # Handle non-integer input safely using try-except.
            print("Error: Please enter a valid integer between 1 and 10.")


def send_telegram_alert(location, severity, victim_name, contact_number):
    """Send accident details to Telegram Bot channel using free Telegram API.

    Returns:
        bool: True if the message is sent successfully, otherwise False.
    """
    # Read Telegram Bot token from environment variable for secure configuration.
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()

    # Stop alert attempt if Telegram Bot token is not configured.
    if not bot_token:
        print("Telegram setup missing: TELEGRAM_BOT_TOKEN not found.")
        print("Get your token from BotFather on Telegram and set it as an environment variable.")
        return False

    # Build the message body with all important accident information.
    message = (
        f"🚨 *ACCIDENT ALERT* 🚨\n\n"
        f"📍 Location: {location}\n"
        f"👤 Victim: {victim_name}\n"
        f"📱 Contact: {contact_number}\n"
        f"⚠️ Severity: {severity}/10\n"
    )

    try:
        # Build Telegram API URL and send message to the demo chat ID.
        url = f"{TELEGRAM_API_URL}{bot_token}/sendMessage"
        payload = {
            "chat_id": DEMO_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown",
        }
        # Send POST request to Telegram with a timeout for reliability.
        response = requests.post(url, json=payload, timeout=10)
        # Check if the Telegram API accepted the message.
        if response.status_code == 200:
            print(f"Alert sent successfully to Telegram chat {DEMO_CHAT_ID}.")
            return True

        # Print API error details when request fails.
        print("Alert sending failed.")
        print(f"Telegram response: {response.json()}")
        return False
    except requests.RequestException as error:
        # Handle network/API exceptions gracefully.
        print(f"Telegram error: {error}")
        return False


def process_accident(location, severity, victim_name, contact_number):
    """Process accident details and print response actions based on severity."""
    # Print a section separator before showing incident details.
    print("\n" + "-" * 70)
    # Show a quick summary of key accident information entered by the user.
    print(f"Location: {location}")
    print(f"Victim Name: {victim_name}")
    print(f"Emergency Contact: {contact_number}")
    print(f"Severity Level: {severity}/10")
    # For demo purposes, always show where the full report is being sent.
    print(f"Demo Telegram Chat ID: {DEMO_CHAT_ID}")
    # Print another separator to separate details from system actions.
    print("-" * 70)
    # Try to send all collected accident information to Telegram.
    print(f"Sending all accident information to Telegram chat {DEMO_CHAT_ID}...")
    send_telegram_alert(location, severity, victim_name, contact_number)

    # Trigger high-priority emergency actions for serious accidents.
    if severity >= 7:
        print("SERIOUS ACCIDENT DETECTED")
        print("Sending emergency alert to nearest hospital...")
        print("Informing victim's family...")
        print("Sharing accident location with emergency services...")
    # Otherwise, mark as minor and monitor the situation.
    else:
        print("MINOR ACCIDENT DETECTED")
        print("Situation is being monitored.")

    # Print an ending separator for clean output formatting.
    print("=" * 70)


def main():
    """Run the interactive simulator loop until the user chooses to exit."""
    # Keep the simulator running until the user explicitly says no.
    while True:
        # Show the main header and current time at the beginning of each cycle.
        display_header()

        # Ask for the accident location input from the user.
        location = input("Enter accident location: ").strip()
        # Ask for the victim's name input from the user.
        victim_name = input("Enter victim name: ").strip()
        # Ask for an emergency contact number.
        contact_number = input("Enter emergency contact number: ").strip()
        # Get a validated severity value using the dedicated function.
        severity = get_severity()

        # Process the collected accident details and print system response.
        process_accident(location, severity, victim_name, contact_number)

        # Ask the user whether to run another simulation cycle.
        retry = input("Do you want to test another accident? (yes/no): ").strip().lower()
        # Keep asking until the user enters a valid yes/no response.
        while retry not in ("yes", "no"):
            print("Error: Please enter 'yes' or 'no'.")
            retry = input("Do you want to test another accident? (yes/no): ").strip().lower()

        # Exit the loop and end the program if the user chooses no.
        if retry == "no":
            print("\nThank you for using the Emergency Accident Alert System.")
            break


# Run the main function only when this script is executed directly.
if __name__ == "__main__":
    main()
