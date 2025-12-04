import requests

def fetch_input(day):
    with open("session_cookie.txt", "r") as session_cookie_file:
        session_cookie = session_cookie_file.read()
        headers = { "Cookie": f"session={session_cookie}" }
        
        url = f"https://adventofcode.com/2025/day/{day}/input"
        
        return requests.get(url, headers=headers).text
