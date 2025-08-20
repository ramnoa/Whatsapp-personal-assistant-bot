from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)

# Example APIs (replace with real ones or expand later)
TECH_API ="https://api.currentsapi.services/v1/latest-news?category=technology&apiKey=VFnpVLyfFnwmOnDuEriSUj0FrFNBBvHoPtLqPVc32GECJ2xC"


MUSIC_API = "https://rss.itunes.apple.com/api/v1/us/itunes-music/new-music/all/10/explicit.rss"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body")
    resp = MessagingResponse()
    reply = resp.message()

    # Normalize message
    msg = incoming_msg.lower() if incoming_msg else ""

    if "tech" in msg:
        # Fetch latest tech headlines (sample)
        try:
            response = requests.get(TECH_API)
            data = response.json()
            headlines = [item['title'] for item in data.get('news', [])][:3]
            reply_text = "Hi Noah 👋, here are the latest tech updates:\n" + "\n".join(headlines)
        except:
            reply_text = "Hi Noah 👋, I couldn't fetch tech updates right now."
        reply.body(reply_text)

    elif "song" in msg or "music" in msg:
        # Fetch trending songs (sample from iTunes RSS)
        try:
            rss = requests.get(MUSIC_API).text
            # Simple parsing (just for titles)
            titles = []
            for line in rss.splitlines():
                if "<title>" in line and "iTunes" not in line:
                    titles.append(line.replace("<title>", "").replace("</title>", "").strip())
            reply_text = "Hi Noah 👋, here are some trending songs:\n" + "\n".join(titles[:5])
        except:
            reply_text = "Hi Noah 👋, I couldn't fetch trending songs right now."
        reply.body(reply_text)

    else:
        reply.body(f"Hi Noah 👋, I didn't quite understand that. Try asking for 'tech updates' or 'new songs'.")

    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
