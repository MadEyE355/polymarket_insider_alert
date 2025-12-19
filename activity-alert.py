import requests
import time

check_time = 35  #min
time_now = int(time.time())

msg = ""

bot_token = "7949811771:AAEG7eywRMob_bFr1WsgsGKqYa8-oCToWjs"
chat_id = "-1002556767038"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    requests.post(url, json=payload)


accounts = [
    ("openai", "0x066d64fa7b2e352b9000a51c6b56f53128cce6e6" , "https://polymarket.com/@RootAccessed"),
    ("openai", "0xdba78eaec18da2455d4b78de38828c2d91f0ae61", "https://polymarket.com/@0xLuck"),
    ("openai", "0x804600942f9044bf4f4ec7f1815b186184e60a1b" , "https://polymarket.com/@Iam100x"),

    ("microstrat" , "0xe5bd36fc97a0bfc002bd2a8afc7616b1074637e7" , "https://polymarket.com/@Ktulhuu"),
    ("microstrat" , "0xf32898291d309e3c5e499c85ddd03a13268c219c" , "https://polymarket.com/@Ktulhu"),
    ("microstrat" , "0x140a8a23e2cb236ec803ad8a8a7da8d68faec075" , "https://polymarket.com/@v4chan"),
    ("microstrat" , "0x64fe36ebdbd3fbdc84a810b6161049e4e0fbe618" , "https://polymarket.com/@Onegambleisenoughtowin"),

    ("csgo" , "0xc60970996247ca70c0195972d2850345c69e7b6f" , "https://polymarket.com/@de-pinya"),

    ("temperature" , "0x6297b93ea37ff92a57fd636410f3b71ebf74517e" , "https://polymarket.com/@neobrother"
]


for i in range(0, len(accounts)):
    url = f"https://data-api.polymarket.com/activity?limit=1&sortBy=TIMESTAMP&sortDirection=DESC&user={accounts[i][1]}"

    response = requests.get(url)
    data = response.json()[0]

    last_activity_time = data["timestamp"]

    last_activity_type = data["type"]
    
    if time_now-last_activity_time < (check_time*60):
        # if last_activity_type == "REDEEM":
            msg = f"activty found \n {last_activity_type} \n {accounts[i][0]} \n {accounts[i][2]}"
            # print(msg)
            send_telegram(msg) 

    
        
    




