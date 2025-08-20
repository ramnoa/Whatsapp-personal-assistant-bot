
# WhatsApp Personal Assistant Bot (Practice Project)

This repository contains a **practice project** for creating a WhatsApp chatbot using **Python, Flask, and Twilio**. The goal of this project is to learn how to:

- Build a WhatsApp chatbot that can receive and respond to messages.
- Integrate **Twilio's WhatsApp Sandbox** for testing.
- Use **ngrok** to expose a local server to the internet.
- Fetch and respond with **real-time content** such as tech news or trending songs.
- Handle incoming messages dynamically using Python.

---

## Features

- Responds to user messages on WhatsApp.
- Fetches the latest tech news using **NewsAPI**.
- Provides trending songs via **iTunes RSS feed**.
- Personalized responses addressing the user by name.

---

## Technologies Used

- **Python 3.12**
- **Flask** – Lightweight web framework
- **Twilio** – WhatsApp API integration
- **Requests** – For HTTP requests to APIs
- **ngrok** – Exposes local server to the internet for testing

---

## Setup Instructions (Practice Use)

1. **Clone the repository:**

```bash
git clone <repository-url>
cd Whatsapp-personal-assistant-bot
Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate   # Windows PowerShell
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask bot:

bash
Copy
Edit
python bot.py
Start ngrok to create a public URL:

bash
Copy
Edit
.\ngrok http 5000
Update Twilio Sandbox webhook with the ngrok URL:

arduino
Copy
Edit
https://<your-ngrok-id>.ngrok-free.app/whatsapp
Send messages to your WhatsApp sandbox number to test responses.

Notes
This project is for learning purposes only.

No sensitive or production-level configurations are included.

The bot demonstrates basic integration with Twilio and API fetching.

Author
Noah Ewalan – Practicing WhatsApp chatbot development.