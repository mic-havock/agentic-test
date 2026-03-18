import requests
import datetime
import os

def get_quote():
    try:
        response = requests.get('https://zenquotes.io/api/random')
        response.raise_for_status()
        data = response.json()
        if data and isinstance(data, list) and len(data) > 0:
            quote = data[0].get('q', 'No quote found')
            author = data[0].get('a', 'Unknown')
            return f'"{quote}" - {author}'
        return "Invalid quote format received."
    except Exception as e:
        print(f"Error fetching quote: {e}")
        return "Could not fetch quote today."

def get_weather():
    try:
        response = requests.get('https://wttr.in/Seattle?format=3')
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return "Could not fetch weather today."

def main():
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quote = get_quote()
    weather = get_weather()

    log_entry = f"## {date_str}\n\n**Quote:** {quote}\n\n**Weather:** {weather}\n\n"

    with open("journal.md", "a", encoding="utf-8") as f:
        f.write(log_entry)

    print(f"Successfully logged entry for {date_str}")

if __name__ == "__main__":
    main()
