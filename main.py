import time
import requests
import os

MOLTBOOK_BASE = "https://moltbook.com"
AGENT_NAME = "son_of_yaman"  # istersek sonra değiştiririz

def register_agent():
    print("📝 Moltbook'a kayıt deneniyor...")
    r = requests.post(
        f"{MOLTBOOK_BASE}/api/agents/register",
        json={"name": AGENT_NAME},
        timeout=15
    )
    r.raise_for_status()
    data = r.json()
    print("✅ Register OK")
    print("🔗 CLAIM LINK:", data.get("claim_url"))
    return data

def heartbeat(token):
    r = requests.post(
        f"{MOLTBOOK_BASE}/api/agents/heartbeat",
        headers={"Authorization": f"Bearer {token}"},
        timeout=15
    )
    r.raise_for_status()
    print("❤️ gerçek heartbeat atıldı")

def main():
    reg = register_agent()
    token = reg.get("token")

    while True:
        heartbeat(token)
        time.sleep(300)  # 5 dk

if __name__ == "__main__":
    main()


